import spacy

'''
CARDINAL, DATE, EVENT, FAC, GPE, LANGUAGE, LAW, LOC, MONEY, NORP,
ORDINAL, ORG, PERCENT, PERSON, PRODUCT, QUANTITY, TIME, WORK_OF_ART

'''


nlp = spacy.load('en_core_web_sm')

text = """
John traveled to the United States with $5000 last monday.
"""

doc = nlp(text)

for ent in doc.ents:
    print(ent.label_,"\t", ent)
