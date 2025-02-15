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
    curr_lesson_hour = ""
    teacher = ""
    type = ""
    lesson = ""
    sub_lesson = ""
    room = ""
    note = ""
    timtable_data = []
    if soup.find("table", {"class": "mon_list"}).tbody:
        tags = soup.find("table", {"class": "mon_list"}).tbody.children  # needed because the html got from requests.get doesnt have tbody in the tables?
    else:
        tags = soup.find("table", {"class": "mon_list"}).children
    for tag in tags:
        if tag == "\n":
            continue  # skip tag elements that are whitespaces
        if (tag.th):  # skip elements with the tag th as a child because they contain labels
            continue
        if tag.td.attrs["class"] == ["list", "inline_header"]:
            curr_class = tag.td.b.string
            print("Class: " + curr_class)
            continue
        for i, sub_tag in enumerate(tag.children):  # class timetable structure: hour, teacher, type, lesson, room, possible note
            match i:
                case 0:
                    curr_lesson_hour = sub_tag.b.string
                    print("Current Hour: " + curr_lesson_hour)
                case 1:
                    pass
                case 2:
                    type = sub_tag.b.string
                    print("Sub. Type: " + type)
                case 3:
                    if len(sub_tag.contents) == 2:
                        lesson = sub_tag.contents[0].string
                        sub_lesson = sub_tag.contents[1].replace("?", "")
                        print(f"Lesson: {lesson}")
                        print(f"Sub. Lesson: {sub_lesson}")
                    else:
                        lesson = sub_tag.string
                        print(f"Lesson: {lesson}")
                case 4:
                    room = sub_tag.b.string
                    print("Room: " + room)
                case 5:
                    pass
        print("------------------------------")
