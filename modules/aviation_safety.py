import requests
from bs4 import BeautifulSoup

"""
Information Derived from Aviation Safety
Data Fields (number = 1)
Safety Records of the Plane
"""

URL = "https://aviation-safety.net/database/registration/regsearch.php?regi="


def get_aviation_safety_data(tail_value):
    updated_url = URL + tail_value
    page = requests.get(updated_url)
    if page.status_code == 200:
        soup= BeautifulSoup(page.content, 'html.parser')
        td  = soup.find('span', {'class': 'nobr'})
        if td:
            r   = requests.get('https://aviation-safety.net'+td.find('a')['href'])
            return r.url
            if r.status_code == 403:
                return 'HTTP 403 while retriving incidents'
    return None