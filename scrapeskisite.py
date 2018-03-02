# _*_coding:utf-8_*_
import requests
from bs4 import BeautifulSoup

FIELDS = ('programgl_czas', 'programgl_impreza', 'programgl_wydarzenie')
stories = []

url = 'http://www.skokinarciarskie.pl/'
ss = requests.Session()
res = ss.get(url)
soup = BeautifulSoup(res.content, 'html5lib')


def interest_tags(tag):
    if tag.name == "div":
        classes = tag.get("class", [])
        return "programgl_data" in classes or \
               "programgl_pole1" in classes or \
               "programgl_pole2" in classes


for czasy in soup.find_all(interest_tags):

    if czasy.attrs == {'class': ['programgl_data']}:
        print(czasy.get_text(), end=' ')

    stories = czasy.find_all('div', class_={FIELDS})
    for ss in stories:
        print(ss.get_text(), end=' ')

    print("")
