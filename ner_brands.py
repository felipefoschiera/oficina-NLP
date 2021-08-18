'''
    Carrega modelo treinado do ner_fashion_brands
    
    - spacy project run preprocess
    - spacy project run train
    - spacy project run evaluate
    - spacy project run visualize-data

'''

import spacy

nlp = spacy.load('packages/...-0.0.0')

text = """

"""

doc = nlp(text)
displacy.serve(doc, style="ent")
