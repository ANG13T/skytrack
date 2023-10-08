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


https://pyflightdata.readthedocs.io/en/latest/pyflightdata.html



# APIs Used
https://weathercams.faa.gov/map/-158.51042,58.49937,-153.28368,59.74111/cameraSite/439/summary

https://airportwebcams.net/igiugig-airport-webcam/

https://aviationstack.com/documentation

http://data.flightradar24.com/zones/fcgi/feed.js?bounds=

https://planefinder.net/endpoints/update.php'\
                    '?callback=planeDataCallback&faa=1&routetype=iata&cfCache=true'\
                    '&bounds=37%2C-80%2C40%2C-74&_=1452535140'


'http://data-live.flightradar24.com/clickhandler/?version=1.5&flight='

https://aviation-safety.net/database/registration/regsearch.php?regi={}

Wikipedia?

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