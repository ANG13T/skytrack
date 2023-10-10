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

def retrieve_value(line, val):
    if val <= len(line) - 1:
        return line[val]
    return None


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

                print(tail_value)

                aircraft = Aircraft(
                    icao24 = retrieve_value(tail_value, 0),
                    registration = retrieve_value(tail_value, 1),
                    manufacturer_icao = retrieve_value(tail_value, 2),
                    manufacturer_name = retrieve_value(tail_value, 3),
                    model = retrieve_value(tail_value, 4),
                    type_code = retrieve_value(tail_value, 5),
                    serial_number = retrieve_value(tail_value, 6),
                    line_number = retrieve_value(tail_value, 7),
                    icao_aircraft_type = retrieve_value(tail_value, 8),
                    operator = retrieve_value(tail_value, 9),
                    operator_callsign = retrieve_value(tail_value, 10),
                    operator_icao = retrieve_value(tail_value, 11),
                    operator_iata = retrieve_value(tail_value, 12),
                    owner = retrieve_value(tail_value, 13),
                    test_registration = retrieve_value(tail_value, 14),
                    registered = retrieve_value(tail_value, 15),
                    reg_valid_until = retrieve_value(tail_value, 16),
                    status = retrieve_value(tail_value, 17),
                    built = retrieve_value(tail_value, 18),
                    first_flight_date = retrieve_value(tail_value, 19),
                    seat_configuration = retrieve_value(tail_value, 20),
                    engines = retrieve_value(tail_value, 21),
                    modes = retrieve_value(tail_value, 22),
                    adsb = retrieve_value(tail_value, 23),
                    acars = retrieve_value(tail_value, 24),
                    notes = retrieve_value(tail_value, 25),
                    category_description = retrieve_value(tail_value, 26)
                )

                aircraft.print()