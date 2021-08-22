# Processamento de Linguagem Natural em Python com spaCy
Oficina (Linux Day 2021) sobre Processamento de Linguagem Natural em Python com spaCy.


### Instalação Linux

```bash
python -m venv .env
source .env/bin/activate
pip install -U pip setuptools wheel
pip install -U spacy
python -m spacy download en_core_web_sm
python -m spacy download pt_core_news_sm
pip install streamlit
```