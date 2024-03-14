"""
Program that scrape the ski website to get all Ski World Cup Events

There must be ski events to see the result data

Example:

python3 scrapeskisite.py

@Author: Darek Duda
@Date: 18.05.2023
@Credit: DarekRepos
@Links: https://github.com/DarekRepos
"""

import requests
from bs4 import BeautifulSoup


def has_event_data_classes(tag):
    """Checks if a tag has classes associated with event data."""
    # Refine search criteria based on HTML structure
    # (consider adding more css class names if needed)
    classes = ["programgl_data", "programgl_pole1", "programgl_pole2", ...]
    return any(event_class in tag.get("class", []) for event_class in classes)


def write_event_data(file, node, fields):
    """Extracts and writes event data from a node."""
    if node.attrs == {"class": ["programgl_data"]}:
        file.write(node.get_text() + " ")
    else:
        events = node.find_all("div", class_=set(fields))
        for event in events:
            file.write(event.get_text() + "|")


def main():
    """
    Main function that program are executed
    """
    fields = ["programgl_czas", "programgl_impreza", "programgl_wydarzenie"]

    url = "http://www.skokinarciarskie.pl/"
    session = requests.Session()
    response = session.get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 "
            + "(Windows NT 10.0; Win64; x64) "
            + "AppleWebKit/537.36 (KHTML, like Gecko) "
            + "Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"
        },
        cookies={"CONSENT": "YES+"},
    )
    soup = BeautifulSoup(response.content, "html.parser")

    with open("SkiEvents.txt", "a+", encoding="utf-8") as file:
        for node in soup.find_all(has_event_data_classes):
            write_event_data(file, node, fields)
            file.write("\n")
        print("Dane zapisano w pliku SkiEvents.txt")


if __name__ == "__main__":
    main()
