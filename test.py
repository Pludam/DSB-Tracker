from parse.parsetimetableresponse import parse_timetable_response
from json import JSONDecoder

from dotenv import load_dotenv
#load .env for user and password
load_dotenv()

with open("response.json","r") as f:
    print(parse_timetable_response(JSONDecoder().decode(f.read())))