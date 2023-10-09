# skytrack
Find information about any airplane given a specific identifier


# Features
- Get latest flown airports
- Get airport information
    - latest flown aircraft
- get general avosint information
- get atc frequency info of airport
- airport webcam links
- get airport diagram
- enter identifier of aircraft or registration or tail number

# APIs Used

https://pyflightdata.readthedocs.io/en/latest/pyflightdata.html

https://weathercams.faa.gov/map/-158.51042,58.49937,-153.28368,59.74111/cameraSite/439/summary

https://airportwebcams.net/igiugig-airport-webcam/

https://aviationstack.com/documentation

https://www.jetphotos.com/photo/keyword/N450FE

https://aviation-safety.net/database/registration/regsearch.php?regi={}

"https://registry.faa.gov/AircraftInquiry/Search/NNumberResult?nNumberTxt="+tail_n

r = requests.get('https://commons.wikimedia.org/wiki/Category:{}_(aircraft)'.format(tail_n))

opensky

Total: 9
Done: 0

# Set Up
Create an account using FlightRadar
https://www.flightradar24.com/premium/signup

# Data Sources

[https://www.icao.int/publications/doc8643/pages/search.aspx](https://www.icao.int/publications/doc8643/pages/search.aspx)
This is the most up to date JSON data file retrieved by the official ICAO Aircraft Type Designators listings webpage


# Information

1. necessary conversions
Convert USA hex to ICAO

ICAO and Tail Numbers follow a mapping system like the following:

ICAO address	N-Number
a00001	N1
a00002	N1A
a00003	N1AA


https://opensky-network.org/datasets/metadata/aircraftDatabase.csv


# Disclaimer
Only works for United States aircraft registrations
The USA hex to ICAO tail number only works for USA registered aircraft

Use the following to learn about Aircraft registration numbers:
https://www.faa.gov/licenses_certificates/aircraft_certification/aircraft_registry/special_nnumbers




# Features 
- tail to ICAO
- get plane information
- generate plane report


# Tail to ICAO Designation Coversion
ICAO Designations are represented by hexadecimal and have a fixed length of 6. This tool only supports U.S. ICAO designations which are denoted by the start letter 'a'. 