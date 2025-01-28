from fetch import get_auth_token,fetch_timetable_data
from parse import parse_timetable_response

from dotenv import load_dotenv
#load .env for user and password
load_dotenv()

print(parse_timetable_response(fetch_timetable_data(get_auth_token())))