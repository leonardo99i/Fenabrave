from bs4 import BeautifulSoup
import urllib3

link_sp = "http://www.fenabrave.org.br/pdf/informativo/automatico/dadosregionais_novo.asp?id=Sao%20Paulo&cap="
page = urllib3.urlopen(link_sp)
soup = BeautifulSoup(page, 'html5lib')
target = soup.find('strong')
print(target)
