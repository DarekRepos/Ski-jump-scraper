# _*_coding:utf-8_*_
import requests
from bs4 import BeautifulSoup


def event_tags(tag):
    if tag.name == "div":
        classes = tag.get("class", [])
        return "programgl_data" in classes or \
               "programgl_pole1" in classes or \
               "programgl_pole2" in classes


def main():
    FIELDS = ('programgl_czas', 'programgl_impreza', 'programgl_wydarzenie')

    url = 'http://www.skokinarciarskie.pl/'
    ss = requests.Session()
    res = ss.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')

    file = open("SkiEvents.txt", "a+")

    for days in soup.find_all(event_tags):

        if days.attrs == {'class': ['programgl_data']}:
            file.write(days.get_text() + " ")

        hours = days.find_all('div', class_={FIELDS})
        for event in hours:
            file.write(event.get_text() + "|")

        file.write("\n")

    print("Dane zapisano w pliku SkiEvents.txt")


if __name__ == '__main__':
    main()
