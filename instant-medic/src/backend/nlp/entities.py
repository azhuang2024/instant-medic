
import imgkit, medspacy, scispacy, spacy
from spacy import displacy

# loads full biomedical corpus ~ 785 words in vocab
nlp = spacy.load("en_core_sci_scibert")
text = """
The patient has stage 4 sarcoma and also stage 2 melanoma. Due to old age, he is inflicted with gouty arthritis and is prone to an aneurysm.
"""
doc = nlp(text)

print(list(doc.sents))
print(doc.ents)

html = displacy.render(doc, style='ent', jupyter=False)
with open(file='entities.html', mode='w') as f:
    f.write(html)
    f.close()
