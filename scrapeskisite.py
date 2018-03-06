# _*_coding:utf-8_*_
import requests
from bs4 import BeautifulSoup


def interest_tags(tag):
    if tag.name == "div":
        classes = tag.get("class", [])
        return "programgl_data" in classes or \
               "programgl_pole1" in classes or \
               "programgl_pole2" in classes


def scrape_skisite():
    FIELDS = ('programgl_czas', 'programgl_impreza', 'programgl_wydarzenie')

    url = 'http://www.skokinarciarskie.pl/'
    ss = requests.Session()
    res = ss.get(url)
    soup = BeautifulSoup(res.content, 'html5lib')

    for days in soup.find_all(interest_tags):

        if days.attrs == {'class': ['programgl_data']}:
            print(days.get_text(), end=' ')

        hours = days.find_all('div', class_={FIELDS})
        for event in hours:
            print(event.get_text(), end=' ')

        print("")


if __name__ == '__main__':
    scrape_skisite()
