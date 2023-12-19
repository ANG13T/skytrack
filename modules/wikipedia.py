import requests

"""
Information Derived from Wikipedia
Data Fields (number = 1)
URL of the specific airplane
"""

def get_wikipedia_data(aircraft, tail_value):
    r = requests.get(
        f'https://commons.wikimedia.org/wiki/Category:{tail_value}_(aircraft)'
    )
    if r.status_code == 200:
        aircraft.Wiki_Link = r.url
    return aircraft