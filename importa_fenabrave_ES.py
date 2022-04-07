#Importação das lib's utilizadas
import pandas as pd
from urllib.request import urlopen
import html
from bs4 import BeautifulSoup
import csv

html = urlopen("http://www.fenabrave.org.br/pdf/informativo/automatico/dadosregionais_novo.asp?id=Esp%EDrito%20Santo&cap=")
soup = BeautifulSoup(html.read(), "html5lib")
extrai_tabela = soup.findAll("table", {"class": "TABELA"})
for tag in extrai_tabela:
        table_str = str(extrai_tabela)
        tabela_pronta = pd.read_html(table_str)[0]
        print(tabela_pronta)

import io
with io.open('UF_ES.csv', "w", encoding="utf-8") as file:
    file.write(str(tabela_pronta))