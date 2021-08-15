'''
    Classes gramaticais:
    https://universaldependencies.org/docs/u/pos/

    - ADJ: adjective                    / adjetivo
    - ADP: adposition                   / adposição (preposições e posposições)
    - ADV: adverb                       / advérbio
    - AUX: auxiliary verb               / verbo auxiliar
    - CONJ: coordinating conjunction    / conjunção
    - DET: determiner                   / determinador
    - INTJ: interjection                / interjeição
    - NOUN: noun                        / substantivo
    - NUM: numeral                      / numeral
    - PART: particle                    / partícula gramatical
    - PRON: pronoun                     / pronome
    - PROPN: proper noun                / nome próprio
    - PUNCT: punctuation                / pontuação
    - SCONJ: subordinating conjunction  / conjunção subordinativa
    - SYM: symbol                       / símbolo
    - VERB: verb                        / verbo
    - X: other                          / outros

'''

import spacy

nlp = spacy.load('pt_core_news_sm')
doc = nlp('O aluno participou do Linux Day na quinta-feira.')

print("{:<15} {:<10} {:<10} {:<10}".format("TEXT", "POS", "TAG", "DEP"))

for token in doc:
    print("{:<15} {:<10} {:<10} {:<10}".format(
        token.text, token.pos_, token.tag_, token.dep_))
