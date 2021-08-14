import spacy

nlp = spacy.load('pt_core_web_sm')
doc = nlp('O aluno participou do Linux Day na quinta-feira.')

for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_,
          token.dep_, token.shape_, token.is_alpa, token.is_stop)
