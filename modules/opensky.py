import os
import requests
import csv
from modules.aircraft import Aircraft

def get_opensky_data(tail_value):
    print("Retrieving Data from Open Sky")
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
            if tail_value in line:
                # Aircraft infos
                icao            = line[0]
                manufacturer    = line[3]
                msn             = line[6]
                # Owner infos
                owner           = line[13]
                return Aircraft(tail_value, 
                            icao=icao,
                            manufacturer=manufacturer,
                            msn=msn),  