from bs4 import BeautifulSoup


# timetable response parsing
def parse_timetable_response(url_response: list) -> dict:
    timetables = {}

    for timetable in url_response:
        timetables[timetable["Title"]] = timetable["Childs"][0]["Detail"]

    return timetables


def parse_timetable_html(html: str) -> dict:
    soup = BeautifulSoup(html, "lxml")
    for tag in soup.find_all("td"):
        print(tag)
