from importlib.resources import contents
import requests
import pandas as pd
from bs4 import BeautifulSoup

requisicao = requests.get('http://www.fenabrave.org.br/pdf/informativo/automatico/dadosregionais_novo.asp?id=Sao%20Paulo&cap=')

if requisicao.status_code == 200:
    print("Sucesso!")
    conteudo = requisicao.content
    soup = BeautifulSoup(conteudo, 'html.parser')
    tabela = soup.find(name='table')
    table_str = str(tabela)
    df = pd.read_html(table_str)[0]