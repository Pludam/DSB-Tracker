import requests

timetable_url = "mobileapi.dsbcontrol.de/dsbtimetables"

def timetablefetch(auth_token) -> list:
    timetable_response = requests.get(timetable_url, params={"authid": auth_token})

    # Check if the request was successful
    if timetable_response.status_code == 200:
        # return the response parsed as json 
        return timetable_response.json()
    else:
        print(f"Request failed with error{timetable_response.text}")