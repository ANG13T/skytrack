
import requests
import os
import csv
from aircraft import Aircraft
from bs4 import BeautifulSoup

def aviationsafety(tail_n, is_verbose):
    r = requests.get('https://aviation-safety.net/database/registration/regsearch.php?regi={}'.format(tail_n))
    
    if r.status_code == 200:
        soup= BeautifulSoup(r.content, 'html.parser')
        td  = soup.find('span', {'class': 'nobr'})
        if td:
            r   = requests.get('https://aviation-safety.net'+td.find('a')['href'])
            return r.url
            if r.status_code == 403:
                return 'HTTP 403 while retriving incidents'
    return None


def flightradar():
    return