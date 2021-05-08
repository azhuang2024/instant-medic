
import spacy, scispacy, texthero as th

from html2image import Html2Image
from IPython.core.display import Image, display_html, display_jpeg
from medspacy.ner import TargetRule
from medspacy.visualization import visualize_ent
from pyate import combo_basic
from spacy import displacy

nlp = spacy.load('en_core_sci_scibert')
# nlp = medspacy.load()
# nlp = medspacy.load("en_core_web_sm", disable={"ner"})
# nlp.add_pipeline(TermExtractionPipeline())


# Add rules for target concept extraction
# target_matcher = nlp.get_pipe("target_matcher")
# target_rules = [
#     TargetRule("atrial fibrillation", "PROBLEM"),
#     TargetRule("atrial fibrillation", "PROBLEM", pattern=[{"LOWER": "afib"}]),
#     TargetRule("pneumonia", "PROBLEM"),
#     TargetRule("Type II Diabetes Mellitus", "PROBLEM", 
#               pattern=[
#                   {"LOWER": "type"},
#                   {"LOWER": {"IN": ["2", "ii", "two"]}},
#                   {"LOWER": {"IN": ["dm", "diabetes"]}},
#                   {"LOWER": "mellitus", "OP": "?"}
#               ]),
#     TargetRule("warfarin", "MEDICATION")
# ]
# target_matcher.add(target_rules)

text = """
The patient has stage 4 sarcoma and also stage 2 melanoma. Due to old age, he is inflicted with gouty arthritis and is prone to an aneurysm.
"""

doc = nlp(text)

entities_html = displacy.render(docs=doc, style='ent')
print(entities_html)
with open(file='entities.html', mode='w') as f:
    f.write(entities_html)
    hti = Html2Image(output_path='/mnt/d/DESKTOP-1S7D2TD/qcaij/OneDrive - University of Florida/DESKTOP-1S7D2TD/qcaij/Desktop/instant-medic/src/backend/nlp')
    hti.screenshot(html_file=f.name, save_as='entities.png')

vis_ent = visualize_ent(doc)
display_jpeg(vis_ent)

# print('-' * 100)
# print(list(doc.sents))
print('-' * 100)
print(list(doc.ents))
# print('-' * 100)
# print(combo_basic("This is just random text."))
# print('-' * 100)

