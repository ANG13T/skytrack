
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

def opensky(tail_n):
    print("[*] Gathering infos from opensky network database. This can take some time")
    headers = {
            'User-Agent': 'SKYTRACK: Aviation-based intelligence gathering tool'\
                    'Information at: https://github.com/ANG13T/skytrack'
    }

    if os.path.exists('/tmp/opensky.cache') \
            and os.stat("/tmp/opensky.cache").st_size != 0:
        print('[*] File exists. Do not download again')

    else:
        r = requests.get(
                'https://opensky-network.org/datasets/metadata/aircraftDatabase.csv',
                stream=True,
                headers=headers)

        if r.status_code == 200:
            with open('/tmp/opensky.cache', 'wb') as f: 
                total_l  = int(r.headers.get('content-length'))
                dl       = 0
                for data in r.iter_content(chunk_size=8192*4):
                    dl += len(data)
                    f.write(data)
                    print('\r[*] Downloading {:2f}'.format((dl/total_l)*100), end='')
                print('\r[*] Done loading !')
        else:
            print(r.status_code)

    with open('/tmp/opensky.cache', 'r') as f:
        parsed_content = csv.reader(f)
        for line in parsed_content:
            if tail_n in line:
                # Aircraft infos
                icao            = line[0]
                manufacturer    = line[3]
                msn             = line[6]
                # Owner infos
                owner           = line[13]
                return Aircraft(tail_n, 
                            icao=icao,
                            manufacturer=manufacturer,
                            msn=msn),  