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


def event_tags(tag):
    """It is function that search for every page elements
    and return children elements node that contain classes
    which event data are inside


    Args:
        tag (string): It is a page element that contain event data ex: "div"

    Returns:
        html node : return page element node for finding events
    """

    event_date_node = "programgl_data"
    word_cup_event_node_1 = "programgl_pole1"
    word_cup_event_node_2 = "programgl_pole2"

    if tag.name == "div":
        classes = tag.get("class", [])
        return (
            event_date_node in classes
            or word_cup_event_node_1 in classes
            or word_cup_event_node_2 in classes
        )
    return None


def main():
    """
    Main function that program are executed
    """
    fields = ("programgl_czas", "programgl_impreza", "programgl_wydarzenie")

    url = "http://www.skokinarciarskie.pl/"
    session = requests.Session()
    response = session.get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 " +
            "(Windows NT 10.0; Win64; x64) " +
            "AppleWebKit/537.36 (KHTML, like Gecko) " +
            "Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"
        },
        cookies={"CONSENT": "YES+"},
    )
    soup = BeautifulSoup(response.content, "html.parser")

    with open("SkiEvents.txt", "a+",  encoding="utf-8") as file:
        # Iterate for every node that contain a day of the event
        # or all events in the Ski World Cup
        for node in soup.find_all(event_tags):
            # write an event date to the file
            if node.attrs == {"class": ["programgl_data"]}:
                file.write(node.get_text() + " ")
            # write all events to  the file for the given date
            events = node.find_all("div", class_={fields})
            for event in events:
                file.write(event.get_text() + "|")

            file.write("\n")
        print("Dane zapisano w pliku SkiEvents.txt")


if __name__ == "__main__":
    main()
