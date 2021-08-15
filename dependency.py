import spacy
from spacy import displacy

nlp = spacy.load('pt_core_news_sm')
doc = nlp('O aluno participou do Linux Day na quinta-feira.')

displacy.serve(doc, style="dep")
