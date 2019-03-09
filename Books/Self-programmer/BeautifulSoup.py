import urllib.request
from bs4 import BeautifulSoup

r = urllib.request.urlopen('https://news.yandex.ru/')
html = r.read()
soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify())
all_a = soup.find_all('a')
for a in all_a:
    print(a.string)
print(soup.get_text())
