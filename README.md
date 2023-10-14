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

https://weathercams.faa.gov/map/-158.51042,58.49937,-153.28368,59.74111/cameraSite/439/summary

https://airportwebcams.net/igiugig-airport-webcam/

https://aviationstack.com/documentation

https://aviation-safety.net/database/registration/regsearch.php?regi={}

https://pkgstore.datahub.io/core/airport-codes/airport-codes/archive/dfadb79d7ba34a49242332f2eaf4f1b0/airport-codes.csv

flight aware

jet photos (done)

wikipedia (done)

opensky (done)

Total: 9
Done: 3

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


# Disclaimer
Only works for United States aircraft registrations
The USA hex to ICAO tail number only works for USA registered aircraft

Use the following to learn about Aircraft registration numbers:
https://www.faa.gov/licenses_certificates/aircraft_certification/aircraft_registry/special_nnumbers


def get_airport_list():
	print('Getting Airport Data.....')
	package = Package('https://datahub.io/core/airport-codes/datapackage.json')
	for resource in package.resources:
	    if resource.descriptor['datahub']['type'] == 'derived/csv':
	        data = resource.read(keyed=True)
	        print('Got Airport Data.....')
	        return data
	return -1


# Features 
- tail to ICAO
- get plane information
- generate plane report


# Tail to ICAO Designation Coversion
ICAO Designations are represented by hexadecimal and have a fixed length of 6. This tool only supports U.S. ICAO designations which are denoted by the start letter 'a'. 


TODO:
add some kind of verification mechanisms


- make a web server version
- deploy the web server version

https://pyfpdf.readthedocs.io/en/latest/


Jinja2 and FPDF:
https://stackoverflow.com/questions/44054938/python-jinja2-putting-all-html-from-python-into-one-pdf-rather-than-multipl