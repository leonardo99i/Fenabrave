#Importação das lib's utilizadas
import pandas as pd
from urllib.request import urlopen
import html
from bs4 import BeautifulSoup
import csv

html = urlopen("http://www.fenabrave.org.br/pdf/informativo/automatico/dadosregionais_novo.asp?id=Sao%20Paulo&cap=")

soup = BeautifulSoup(html.read(), "html5lib")
extrai_tabela = soup.findAll("table", {"class": "TABELA"})
for tag in extrai_tabela:
        table_str = str(extrai_tabela)
        df = pd.read_html(table_str)[0]
        print(df)




