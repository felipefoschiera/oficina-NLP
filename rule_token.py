'''
    Token Matcher com um token
'''
import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)

# Cria um padrão "<hello><pontuacao><world>" identificado por "HelloWorld"
pattern = [{"LOWER": "hello"}, {"IS_PUNCT": True}, {"LOWER": "world"}]
matcher.add("HelloWorld", [pattern])

doc = nlp("Hello, world! Hello world!")
matches = matcher(doc)
for match_id, start, end in matches:
    string_id = nlp.vocab.strings[match_id]  # Nome do padrão
    span = doc[start:end]  # Trecho de texto do match
    print(match_id, string_id, start, end, span.text)
