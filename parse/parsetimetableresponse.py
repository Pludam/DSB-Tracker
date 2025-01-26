
def parse_timetable_response(url_response:list)->dict:
    timetables = {}
    
    for timetable in url_response:
        timetables[timetable["Title"]] = timetable["Childs"][0]["Detail"]

    return timetables