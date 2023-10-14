import os
import requests
import csv
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

def get_opensky_data(aircraft, tail_value):
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

                aircraft.ICAO24 = retrieve_value(line, 0)
                aircraft.Registration = retrieve_value(line, 1)
                aircraft.Manufacturer_ICAO = retrieve_value(line, 2)
                aircraft.Manufacturer_Name = retrieve_value(line, 3)
                aircraft.Model = retrieve_value(line, 4)
                aircraft.Type_Code = retrieve_value(line, 5)
                aircraft.Serial_Number = retrieve_value(line, 6)
                aircraft.Line_Number = retrieve_value(line, 7)
                aircraft.ICAO_Aircraft_Type = retrieve_value(line, 8)
                aircraft.Operator = retrieve_value(line, 9)
                aircraft.Operator_Callsign = retrieve_value(line, 10)
                aircraft.Operator_ICAO = retrieve_value(line, 11)
                aircraft.Operator_IATA = retrieve_value(line, 12)
                aircraft.Owner = retrieve_value(line, 13)
                aircraft.Test_Registration = retrieve_value(line, 14)
                aircraft.Registered = retrieve_value(line, 15)
                aircraft.Registration_Valid_Until = retrieve_value(line, 16)
                aircraft.Status = retrieve_value(line, 17)
                aircraft.Built = retrieve_value(line, 18)
                aircraft.First_Flight_Date = retrieve_value(line, 19)
                aircraft.Seat_Configuration = retrieve_value(line, 20)
                aircraft.Engines = retrieve_value(line, 21)
                aircraft.Modes = retrieve_value(line, 22)
                aircraft.ADSB = retrieve_value(line, 23)
                aircraft.ACARS = retrieve_value(line, 24)
                aircraft.Notes = retrieve_value(line, 25)
                aircraft.Category_Description = retrieve_value(line, 26)

                aircraft.print()

                return aircraft

    return aircraft