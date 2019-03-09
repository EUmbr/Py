import requests
import re
from bs4 import BeautifulSoup


url1 = 'https://stepic.org/media/attachments/lesson/24472/sample0.html'

url2 = 'https://stepic.org/media/attachments/lesson/24472/sample2.html'
rec = requests.get(url1).content.decode("utf-8")

soup = BeautifulSoup(rec, "html.parser")
urls = []
flag = False

for link in soup.find_all("a"):
    urls.append(link.get("href"))

for link in urls:
    new_soup = BeautifulSoup(requests.get(link).content.decode("utf-8"), "html.parser")
    for links in new_soup.find_all('a'):
        new_url = links.get('href')
        if new_url == url2:
            flag = True


if flag:
    print('Yes')
else:
    print('No')
