import spacy
from spacy import displacy

nlp = spacy.load('pt_core_news_lg')

text = """
A Xiaomi ultrapassou a Apple (AAPL) e se tornou a segunda maior fabricante de smartphones do mundo pela primeira vez, de acordo com a empresa de pesquisa de mercado Canalys.

A empresa chinesa recebeu 17% das remessas mundiais de smartphones no segundo trimestre de 2021, atrás dos 19% da Samsung, disse a Canalys em relatório publicado na quinta-feira (15). Em comparação com o mesmo período de 2020, as remessas da Xiaomi aumentaram mais de 80%.

A Apple ficou em terceiro lugar, com remessas que representaram 14% do total global. As fabricantes chinesas de smartphones Oppo e Vivo seguiram, com 10% cada. 
O relatório da Canalys mede o número de fabricantes de aparelhos que vendem aos distribuidores.

Esta é a primeira vez que Xiaomi fica em segundo lugar no relatório Canalys. No primeiro trimestre de 2021 e durante todo o ano de 2020, Samsung (SSNLF) e Apple (AAPL) foram as duas principais marcas de smartphones do mundo. Em 2019, Samsung e Huawei lideraram a lista.

Tornar-se o segundo fornecedor do mundo é um "marco importante na história da Xiaomi", disse Lei Jun, fundador e CEO da Xiaomi, em uma carta aos funcionários na sexta-feira (15).

"Apesar das celebrações agora, quero ter certeza de que podemos manter nosso segundo lugar de forma constante e firme no futuro", disse ele.

As ações da Xiaomi subiram quase 5% em Hong Kong na sexta.

A expansão global da Xiaomi e sua estratégia de varejo — a companhia quer que suas lojas online e físicas trabalhem juntas de forma mais integrada — impulsionou seu crescimento nas remessas no segundo trimestre, disse a empresa em um comunicado.

O gerente de pesquisa da Canalys, Ben Stanton, também disse no relatório que a Xiaomi está "vendo um crescimento rápido em seus negócios no exterior".
"""

doc = nlp(text)

displacy.serve(doc, style="ent")
