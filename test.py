from fetch import get_auth_token,fetch_timetable_data
from parse import parse_timetable_response, parse_timetable_html
from dotenv import load_dotenv
import requests
#load .env for user and password
load_dotenv()

timetableresponse = parse_timetable_response(fetch_timetable_data(get_auth_token()))
print(timetableresponse)





parse_timetable_html(requests.get(timetableresponse["Schülerplan Heute - subst_001"]).text)
