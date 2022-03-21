#Importação das bibliotecas utilizadas
from cgitb import html #Biblioteca
from urllib.request import urlopen #Abre a pagina html
from urllib.error import HTTPError
from urllib.error import URLError  #Informa se ocorre erro na requisição
from bs4 import BeautifulSoup #Biblioteca que vai fazer o web scraping e capturar os dados que queremos

try:
    #Link do fenabrave para download
    html = urlopen("http://www.fenabrave.org.br/pdf/informativo/automatico/dadosregionais_novo.asp?id=Sao%20Paulo&cap=")
    #Check para saber se a página abre ou não
except HTTPError as html:
    print(html)
except URLError:
    print("Servidor fora do ar ou dominio incorreto")
else:
    procura = BeautifulSoup(html.read(), "html5lib")
    extrai = procura.findAll("table", {"class": "TABELA"})
    for tag in extrai:
        print(tag.getText())

    