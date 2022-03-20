from cgitb import html
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

try:
    html = urlopen("http://www.fenabrave.org.br/pdf/informativo/automatico/dadosregionais_novo.asp?id=Sao%20Paulo&cap=")
except HTTPError as e:
    print(e)
except URLError:
    print("Servidor fora do ar ou dominio incorreto")
else:
    res = BeautifulSoup(html.read(), "html5lib")
    tags = res.findAll("table", {"class": "TABELA"})
    for tag in tags:
        print(tag.getText())