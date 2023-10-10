import requests

"""
Information Derived from Wikipedia
Data Fields (number = 1)
URL of the specific airplane
"""

def get_wikipedia_data(aircraft, tail_value):
    r = requests.get('https://commons.wikimedia.org/wiki/Category:{}_(aircraft)'.format(tail_value))
    if r.status_code == 200:
        aircraft.Wiki_Link = r.url
        return aircraft
    else:
        return aircraft