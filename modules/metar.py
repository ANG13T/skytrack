import requests
"""
Information Derived from Aviation Weather
Data Fields (number = 1)
METAR information
Date (yyyymmdd_hhmm)

"""

URL = "https://aviationweather.gov/cgi-bin/data/metar.php?ids={}&format=decoded"


def get_metar_data(airport_ident, time):
    if airport_ident == None or time == None:
        return None
    updated_url = URL.format(airport_ident)
    page = requests.get(updated_url)
    print(page)

def convert_time(time_string):
    return