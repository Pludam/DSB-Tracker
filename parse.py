from bs4 import BeautifulSoup
from util import format_line
from collections import defaultdict

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
    sub_teacher = ""
    type = ""
    lesson = ""
    sub_lesson = ""
    room = ""
    note = ""
    timetable_data = defaultdict(dict)
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
            continue
        for i, sub_tag in enumerate(tag.children):
            match i:
                case 0:# hour
                    curr_lesson_hour = sub_tag.b.string
                case 1:# teacher
                    if len(sub_tag.contents) == 2:
                        teacher = sub_tag.contents[0].string
                        sub_teacher = sub_tag.contents[1].replace("?", "")
                    else:
                        lesson = sub_tag.string
                case 2:# type
                    type = sub_tag.b.string
                case 3:# lesson
                    if len(sub_tag.contents) == 2:
                        lesson = sub_tag.contents[0].string
                        sub_lesson = sub_tag.contents[1].replace("?", "")
                    else:
                        lesson = sub_tag.string
                case 4:# room
                    room = sub_tag.b.string.replace(u'\xa0', u'')
                case 5:# note
                    note = sub_tag.b.string.replace(u'\xa0', u'')
        timetable_data[curr_class][curr_lesson_hour] = {"teacher": teacher, "sub_teacher":sub_teacher, "type": type, "lesson": lesson, "sub_lesson": sub_lesson, "room": room, "note": note}
    return timetable_data