# skytrack
Find information about any airplane given a specific identifier


# Features
- Get latest flown airports
- Get airport information
    - latest flown aircraft
- get general avosint information
- get atc frequency info of airport
- enter identifier of aircraft or registration or tail number

# APIs Used
metar (done)

airport information (done)

aviation safety (done)

flight aware (done)

jet photos (done)

wikipedia (done)

opensky (done)

# Set Up

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

finish:

- print output of osint in a pretty way

- generate PDF
- format data visualization from telemetry
- run additional tests

- write README
- make cool banner and icon
- share on Linkedin, Reddit, GitHub, Twitter, and Discord