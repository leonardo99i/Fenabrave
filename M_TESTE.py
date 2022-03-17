from urllib.request import urlopen
from venv import create
from bs4 import BeautifulSoup
import xlsxwriter 

url = "http://www.fenabrave.org.br/pdf/informativo/automatico/dadosregionais_novo.asp?id=Sao%20Paulo&cap="
html = urlopen(url).read()
soup = BeautifulSoup(html, features="html.parser")

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)

print(text)


workbook = xlsxwriter.Workbook('hello.xlsx') 
worksheet = workbook.add_worksheet() 
worksheet.write('A1', text) 