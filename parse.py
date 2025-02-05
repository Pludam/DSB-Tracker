from bs4 import BeautifulSoup
from util import format_line

# timetable response parsing
@format_line
def parse_timetable_response(url_response: list) -> dict:
    timetables = {}

    for timetable in url_response:
        timetables[timetable["Title"]] = timetable["Childs"][0]["Detail"]
    print(timetables)
    return timetables


def parse_timetable_html(html: str) -> dict:
    soup = BeautifulSoup(html, "lxml")
    
    for i,tag in enumerate(soup.find("table", {"class": "mon_list"}).children):
        if i == 1:
            continue
        if i % 2: # needed because every second element is apparently a whitespace?
            print(i,tag)  
        
        
