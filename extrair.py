import urllib.request
from bs4 import BeautifulSoup

link_sp = "http://www.fenabrave.org.br/pdf/informativo/automatico/dadosregionais_novo.asp?id=Sao%20Paulo&cap="
abre_pagina = urllib.request.urlopen(link_sp)
soup = BeautifulSoup(abre_pagina, 'html.parser')
busca_item = soup.find('tbody')
extrai_valor = busca_item.text.split()
print(busca_item)