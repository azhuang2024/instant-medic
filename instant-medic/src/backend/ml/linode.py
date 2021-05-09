
import os
from linode_api4 import LinodeClient, Instance
from dotenv import load_dotenv

load_dotenv()
TOKEN1 = os.getenv(key='TOKEN1')
CLIENT_ID = os.getenv(key='CLIENT_ID')

client = LinodeClient(TOKEN1)
available_regions = client.regions()
chosen_region = available_regions[0]
print(chosen_region)

my_linodes = client.linode.instances()
for current_linode in my_linodes:
    print(current_linode.label)

my_linode = Instance(client, CLIENT_ID)
# loaded_linode = client.load(my_linode, CLIENT_ID)
print(my_linode)
