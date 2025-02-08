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
    curr_class = ""
    lesson_hour = ""
    teacher = ""
    sub_type = ""
    room = ""
    notes = ""
    for tag in soup.find("table", {"class": "mon_list"}).children:
        if tag  == "\n":
            continue # skip tag elements that are whitespaces 
        if tag.th: # skip elements with the tag th as a child because they contain labels
            continue
        if tag.td.attrs["class"] == ["list","inline_header"]:
            curr_class = tag.td.b.string
            print(curr_class)
            continue
        for i,sub_tag in enumerate(tag.children): # class timetable structure: hour, teacher, type, lesson, room, possible notes
            pass
            

        
        
