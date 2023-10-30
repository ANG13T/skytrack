import requests
from bs4 import BeautifulSoup

"""
Information Derived from Jet Photos
Data Fields (number = 1)
Photos of the Plane (max photos = 3)
"""

URL = "https://www.jetphotos.com/photo/keyword/"


def get_jetphotos_data(tail_value):
    updated_url = URL + tail_value
    page = requests.get(updated_url)
    soup = BeautifulSoup(page.content, "html.parser")
    images = soup.find_all("img", {"class": "result__photo"})

    if len(images) == 0:
        return []

    result = []
    for image in images:
        result.append("https:" + image['src'])

    if len(result) > 3:
        return result[:3]
    else:
        return result
