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

    Frases:
    - O aluno participou do Linux Day na quinta-feira.
    - A Apple lançou um produto muito caro na semana passada.
'''

dicionario = {
    'ADJ': 'ADJETIVO',
    'ADP': 'ADPOSIÇÃO',
    'ADV': 'ADVÉRBIO',
    'AUX': 'VERBO AUXILIAR',
    'CONJ': 'CONJUNÇÃO',
    'DET': 'DETERMINADOR',
    'INTJ': 'INTERJEIÇÃO',
    'NOUN': 'SUBSTANTIVO',
    'NUM': 'NUMERAL',
    'PART': 'PARTÍCULA GRAMATICAL',
    'PRON': 'PRONOME',
    'PROPN': 'NOME PRÓPRIO',
    'PUNCT': 'PONTUAÇÃO',
    'SCONJ': 'CONJUNÇÃO SUBORDINATIVA',
    'SYM': 'SÍMBOLO',
    'VERB': 'VERBO'
}

import spacy

nlp = spacy.load('pt_core_news_sm')
doc = nlp('A Apple lançou um produto muito caro na semana passada.')

print("{:<15} {:<10} {:<10} {:<10} {:<20}".format("TEXT", "POS", "TAG", "DEP", "CLASSE"))

for token in doc:
    classe = None
    if token.pos_ in dicionario:
        classe = dicionario[token.pos_]
    print("{:<15} {:<10} {:<10} {:<10} {:<20}".format(
        token.text, token.pos_, token.tag_, token.dep_, classe))
