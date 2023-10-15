import os
import requests
import csv
from modules.file_formatter import format_file_name
from modules.models.airport import Airport

'''
Information Derived from Airport Codes
Data Fields (number = 12)

ident: Unique identifier or code for the location (e.g., airport).

type: Type or category of the location (e.g., small airport, large airport).

name: Name of the location (e.g., airport name, city name).

elevation_ft: Elevation of the location in feet.

continent: Continent on which the location is situated.

iso_country: ISO code for the country where the location is located.

iso_region: More detailed regional code within a country.

municipality: Name of the municipality or city.

gps_code: GPS code associated with the location.

iata_code: IATA code for the location (used in the airline industry).

local_code: Local code or identifier for the location.

coordinates: Geographic coordinates (latitude, longitude) of the location.
'''

URL = "https://pkgstore.datahub.io/core/airport-codes/airport-codes/archive/dfadb79d7ba34a49242332f2eaf4f1b0/airport-codes.csv"
cache_path = format_file_name("./tmp/airports.cache")

def retrieve_value(line, val):
    if val <= len(line) - 1:
        return line[val]
    return None

def get_airport_info(airport_ident, airport_name):
    print("Retrieving Airport Codes")
    headers = {
        'User-Agent': 'SKYTRACK: Aviation-based intelligence gathering tool'\
        'Information at: https://github.com/ANG13T/skytrack'
    }

    if not os.path.exists(cache_path) or os.stat(cache_path).st_size == 0:
        r = requests.get(
                URL,
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
            print(line, airport_ident, airport_name, airport_ident in line, airport_name in line)
            if airport_ident in line[0] and airport_name in line[2]:

                print(airport_ident)
                airport = Airport()

                airport.ident = retrieve_value(line, 0)
                airport.type = retrieve_value(line, 1)
                airport.name = retrieve_value(line, 2)
                airport.elevation_ft = retrieve_value(line, 3)
                airport.continent = retrieve_value(line, 4)
                airport.iso_country = retrieve_value(line, 5)
                airport.iso_region = retrieve_value(line, 6)
                airport.municipality = retrieve_value(line, 7)
                airport.gps_code = retrieve_value(line, 8)
                airport.iata_code = retrieve_value(line, 9)
                airport.local_code = retrieve_value(line, 10)
                airport.coordinates = retrieve_value(line, 11)

                return airport

    return None