from bs4 import BeautifulSoup

code = '''
<td width="87" align="center" valign="middle" class="b_inf b_dir fndo">
<strong>&nbsp;24241</strong>
</td>
'''

soup = BeautifulSoup(code)

tag_strong = soup.td.strong  

print(tag_strong.text)
print(tag_strong['href'])