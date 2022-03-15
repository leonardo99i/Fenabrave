import urllib.request
from bs4 import BeautifulSoup

link = "http://www.fenabrave.org.br/pdf/informativo/automatico/dadosregionais_novo.asp?id=Sao%20Paulo&cap="
page = urllib.request.urlopen(link)
soup = BeautifulSoup(page, 'html5lib')

list_item = soup.find('strong', attrs={'class': 'b_inf b_dir fndo'})
imprimi =list_item.text.strip()
print(imprimi)