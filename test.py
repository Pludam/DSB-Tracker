from parse.parsetimetableresponse import parse_timetable_response
from json import JSONDecoder

with open("response.json","r") as f:
    print(parse_timetable_response(JSONDecoder().decode(f.read())))