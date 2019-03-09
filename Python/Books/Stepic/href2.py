import requests
import re
from bs4 import BeautifulSoup

url = 'http://pastebin.com/raw/7543p0ns'
rec = requests.get(url).content.decode("utf-8")
soup = BeautifulSoup(rec, "html.parser")
s = []
for link in soup.find_all('a'):
    li = link.get('href')
    if li:
        num = li[7:].find('/') + 7
        s.append(li[7:num])

s = sorted(set(s))
for _ in s:
    print(_)
