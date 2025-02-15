from fetch import get_auth_token,fetch_timetable_data
from parse import parse_timetable_response, parse_timetable_html
from dotenv import load_dotenv
import requests
#load .env for user and password
load_dotenv()

timetableresponse = parse_timetable_response(fetch_timetable_data(get_auth_token()))

local = True




with open("timetable_response.html","w") as t:
    t.write(requests.get(timetableresponse["Schülerplan Morgen - subst_001"]).text)


if local:
#parse_timetable_html(requests.get(timetableresponse["Schülerplan Morgen - subst_001"]).text)
    with open("example_timetable_browser.htm") as timetable:
        
        timetable_html = timetable.read()
        parse_timetable_html(timetable_html)
else:
    parse_timetable_html(requests.get(timetableresponse["Schülerplan Morgen - subst_001"]).text)