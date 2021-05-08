
import io, os

from google.cloud import vision_v1p3beta1 as vision
from google.oauth2 import service_account
from dotenv import load_dotenv

# loading credentials
load_dotenv()
KEY_PATH = os.getenv(key='KEY_PATH')
credentials = service_account.Credentials.from_service_account_file(filename=KEY_PATH)
client = vision.ImageAnnotatorClient(credentials=credentials)

def detect_text(path: str):
    """Detects text in the file.

    Args:
        path (str): Path to image.

    Raises:
        Exception: Response has error.
    """
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')

    for text in texts:
        print(f'\n{text.description}')
        vertices = ([f'({vertex.x}, {vertex.y})' for vertex in text.bounding_poly.vertices])
        print(f'bounds: {",".join(vertices)}')

    if response.error.message:
        raise Exception(f'{response.error.message}\nFor more info on error messages, check: https://cloud.google.com/apis/design/errors')

def detect_text_uri(uri: str):
    """Detects text in the file located in Google Cloud Storage or on the Web.

    Args:
        uri (str): URI of image.

    Raises:
        Exception: Response has error.
    """

    image = vision.Image()
    image.source.image_uri = uri
    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')

    for text in texts:
        print(f'\n{text.description}')
        vertices = ([f'({vertex.x}, {vertex.y})' for vertex in text.bounding_poly.vertices])
        print(f'bounds: {",".join(vertices)}')

    if response.error.message:
        raise Exception(f'{response.error.message}\nFor more info on error messages, check: https://cloud.google.com/apis/design/errors')

if __name__ == '__main__':
    path='Ep3_junior.jpg'
    uri = 'https://image.zmenu.com/menupic/1275901/c751e781-c4f1-4947-866b-8557bbb8e336.jpg'
    print('-' * 100)
    detect_text(path=path)
    print('-' * 100)
    detect_text_uri(uri=uri)
