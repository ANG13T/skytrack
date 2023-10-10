import os
import requests
import csv
from modules.aircraft import Aircraft
from modules.file_formatter import format_file_name

"""
Information Derived from Open Sky 
Data Fields (number = 27)

icao24: String - Unique identifier assigned by the International Civil Aviation Organization (ICAO) to the aircraft.

registration: String - Aircraft registration number.

manufacturericao: String - ICAO code for the aircraft manufacturer.

manufacturername: String - Name of the aircraft manufacturer.

model: String - Model of the aircraft.

typecode: String - Type code associated with the aircraft.

serialnumber: String - Serial number of the aircraft.

linenumber: String - Line number of the aircraft.

icaoaircrafttype: String - ICAO aircraft type code.

operator: String - Company or entity that operates the aircraft.

operatorcallsign: String - Callsign used by the operator.

operatoricao: String - ICAO code of the operator.

operatoriata: String - IATA code of the operator.

owner: String - Owner of the aircraft.

testreg: String - Test registration information.

registered: String (Date format, e.g., "2027-01-31") - Date when the aircraft was registered.

reguntil: String (Date format, e.g., "2027-01-31") - Date until which the registration is valid.

status: String - Current status of the aircraft.

built: String (Year, e.g., "1967") - Year when the aircraft was built.

firstflightdate: String (Date format, e.g., "1967-01-01") - Date of the first flight of the aircraft.

seatconfiguration: String - Configuration of seats in the aircraft.

engines: String - Information about the aircraft's engines.

modes: String - Information about the aircraft's modes.

adsb: String ("true" or "false") - ADS-B (Automatic Dependent Surveillance–Broadcast) status.

acars: String ("true" or "false") - ACARS (Aircraft Communications Addressing and Reporting System) status.

notes: String - Additional notes or comments.

categoryDescription: String - Description of the aircraft category.
"""

cache_path = format_file_name("./tmp/opensky.cache")

def get_opensky_data(tail_value):
    print("Retrieving Data from Open Sky")
    headers = {
        'User-Agent': 'SKYTRACK: Aviation-based intelligence gathering tool'\
        'Information at: https://github.com/ANG13T/skytrack'
    }

    if not os.path.exists(cache_path) or os.stat(cache_path).st_size == 0:
        r = requests.get(
                'https://opensky-network.org/datasets/metadata/aircraftDatabase.csv',
                stream=True,
                headers=headers)

        if r.status_code == 200:
            if not os.path.exists(os.path.dirname(cache_path)):
                os.makedirs(os.path.dirname(cache_path))

            with open(cache_path, 'wb') as f: 
                total_l  = int(r.headers.get('content-length'))
                dl       = 0
                for data in r.iter_content(chunk_size=8192*4):
                    dl += len(data)
                    f.write(data)
                    print('\r[*] Downloading {:2f}'.format((dl/total_l)*100), end='')
                print('\r[*] Done loading !')
        else:
            print(r.status_code)

    with open(cache_path, 'r') as f:
        result = csv.reader(f)
        for line in result:
            if tail_value in line:

                icao            = line[0]
                manufacturer    = line[3]
                msn             = line[6]
                owner           = line[13]

                return Aircraft(
                    tail_value,
                    icao=icao,
                    manufacturer=manufacturer,
                    msn=msn
                )