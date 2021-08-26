import spacy
from spacy import displacy

nlp = spacy.load('pt_core_news_sm')
doc = nlp('A Apple lançou um produto muito caro na semana passada.')

displacy.serve(doc, style="dep")
