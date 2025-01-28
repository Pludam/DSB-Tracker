import requests
import datetime
from os import getenv

#auth stuff
token = ""
# Iso format is for example 2019-10-29T19:20:31.875466
current_time = datetime.datetime.now().isoformat()
# Cut off last 3 digits and add 'Z' to get correct format
current_time = current_time[:-3] + "Z"

auth_url = "https://mobileapi.dsbcontrol.de/authid"

auth_params = {
            "bundleid": "de.heinekingmedia.dsbmobile",
            "appversion": "36",
            "osversion": "22",
            "pushid": "",
            "user": getenv("DSB_User"),
            "password": getenv("DSB_Password")
        }




def get_auth_token()-> str:
    

    auth_response = requests.get(auth_url, params=auth_params)

    if auth_response.text == "\"\"": # Me when http status code is always 200 :trollface:
                raise Exception("Invalid Credentials")
    else:
        token = auth_response.text.replace("\"", "")
        return token
    
#timetable stuff
timetable_url = "https://mobileapi.dsbcontrol.de/dsbtimetables"

def fetch_timetable_data(auth_token) -> list:
    timetable_response = requests.get(timetable_url, params={"authid": auth_token})

    # Check if the request was successful
    if timetable_response.status_code == 200:
        # return the response parsed as json 
        return timetable_response.json()
    else:
        print(f"Request failed with error{timetable_response.text}")