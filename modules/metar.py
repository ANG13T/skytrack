import requests

"""
Information Derived from Aviation Weather
Data Fields (number = 1)
METAR information as text
Date (2023-10-22T22:31:44Z format)
"""

URL = "https://aviationweather.gov/cgi-bin/data/metar.php?ids={}&date={}&format=decoded"


def get_metar_data(airport_ident, time):
    if airport_ident == None or time == None:
        return None
    updated_url = URL.format(airport_ident, time)
    page = requests.get(updated_url)
    if page.status_code == 200:
        return page.text
    return None