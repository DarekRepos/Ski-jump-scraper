"""
Program that scrape the ski website to get all Ski World Cup Events

There must be ski events to see the result data

Example:

python3 scrapeskisite.py

Example:

>>> from scrapeskisite import scrape
>>> scrape()
Data saved to the file SkiEvents.txt

@Author: Darek Duda
@Date: 18.05.2023
@Credit: DarekRepos
@Links: https://github.com/DarekRepos
"""

import requests
from bs4 import BeautifulSoup


def has_event_data_classes(tag):
    """
    Checks if a tag has classes associated with event data.

    Args:
    tag (bs4.element.Tag): The BeautifulSoup Tag object.

    Returns:
    bool: True if the tag has classes associated with event data, False otherwise.

    >>> from bs4 import BeautifulSoup
    >>> tag = BeautifulSoup('<div class="programgl_data"></div>', 'html.parser').div
    >>> has_event_data_classes(tag)
    True
    """
    # Refine search criteria based on HTML structure
    # (consider adding more css class names if needed)
    classes = ["programgl_data", "programgl_pole1", "programgl_pole2", ...]
    return any(event_class in tag.get("class", []) for event_class in classes)


def write_event_data(file, node, fields):
    """
    Extracts and writes event data from a node.

    Args:
    file (file object): The file object to write event data.
    node (bs4.element.Tag): The BeautifulSoup Tag object containing event data.
    fields (list): A list of field classes to search for within the node.

    >>> from bs4 import BeautifulSoup
    >>> with open('test.txt', 'w') as file:
    ...     node = BeautifulSoup('<div class="programgl_data">Event Data</div>', 'html.parser').div
    ...     fields = ["programgl_czas", "programgl_impreza", "programgl_wydarzenie"]
    ...     write_event_data(file, node, fields)
    >>> with open('test.txt', 'r') as file:
    ...     file.read()
    'Event Data '
    """
    if node.attrs == {"class": ["programgl_data"]}:
        file.write(node.get_text() + " ")
    else:
        events = node.find_all("div", class_=set(fields))
        for event in events:
            file.write(event.get_text() + "|")


def scrape():
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
        print("Data saved to the file SkiEvents.txt")


if __name__ == "__main__":
    scrape()
