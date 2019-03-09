import urllib.request
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        sp = BeautifulSoup(html, 'html.parser')
        for tag in sp.find_all("div"):

            url = tag.get("class")
            if url is None:
                continue
            if "ng-star-inserted" in url:
                print("\n" + url)


news = "http://ruz.hse.ru/ruz/main"
Scraper(news).scrape()
