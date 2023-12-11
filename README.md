

## What is Plane Spotting?
Plane spotting is the art of 

## About
skytrack is a command-line based plane spotting and aircraft OSINT reconnaissance tool made using Python.
It can gather aircraft information using various data sources, generate a PDF report for a specified aircraft, and convert between ICAO and Tail Number designations. 

## Preview

<img alt="DroneXtract logo" width="600" src="https://github.com/ANG13T/DroneXtract/blob/main/assets/Preview.png">

## Information Gathered
- Tail Number 🛫
- Aircraft Type ⚙️
- ICAO24 Designation 🔎
- Manufacturer Details 🛠
- Flight Logs 📄 
- Aircraft Owner ✈️
- Model 🛩
- Much more!

## Features
DroneXtract features four main suites for drone forensics and auditing. They include the following:

### Aircraft Reconnaissance & OSINT
You can visualize and extract information from DJI file formats such as CSV, KML, and GPX using the parsing tool.
The parsed information can be saved into an alternative file format when inputted an output file path.
The image below includes an example of a parsed file output and the type of data extracted from the file.

<img alt="DroneXtract logo" height="300" src="https://github.com/ANG13T/DroneXtract/blob/main/assets/demo-1.png">


### PDF Aircraft Information Report
Steganography refers to the process of revealing information stored within files.
The DroneXtract steganography suite allows you to extract telemetry and valuable data from image and video formats.
Additionally, the extracted data can be exported to four different file formats.

<img alt="DroneXtract logo" height="300" src="https://github.com/ANG13T/DroneXtract/blob/main/assets/demo-2.png">

### Tail Number to ICAO Converter
There are two standard identification formats for specifying aircraft: Tail Number and ICAO Designation. The tail number (aka N-Number) is a alphanumerical ID starting with the letter "N" used to identify aircraft. The ICAO type designation is a six character fixed-length ID in the hexadecimal format. 
Both standards are highly pertinent for aircraft reconnnaisance as they both can be used to search for a specific aircraft in data sources.
However, converting them from one format to another can be rather cumbersome as it follows a tricky algorithm. To streamline this process, skytrack includes a standard converter. 

### Explaination

ICAO and Tail Numbers follow a mapping system like the following:

ICAO address	N-Number (Tail Number)
a00001	        N1
a00002	        N1A
a00003	        N1AA



#### Disclaimer
Only works for United States aircraft registrations
The USA hex to ICAO tail number only works for USA registered aircraft

You can learn more about aircraft registration numbers [here](https://www.faa.gov/licenses_certificates/aircraft_certification/aircraft_registry/special_nnumbers)


<img alt="DroneXtract logo" width="600" src="https://github.com/ANG13T/DroneXtract/blob/main/assets/demo-3.png">


## Usage
To run skytrack on your machine, follow the steps below:

```bash
$ git clone https://github.com/ANG13T/skytrack
$ cd skytrack
$ python skytrack.py
```

skytrack works best for Python version 3.

## Data Sources & APIs Used
[https://www.icao.int/publications/doc8643/pages/search.aspx](https://www.icao.int/publications/doc8643/pages/search.aspx)
This is the most up to date JSON data file retrieved by the official ICAO Aircraft Type Designators listings webpage

metar (done)

airport information (done)

aviation safety (done)

flight aware (done)

jet photos (done)

wikipedia (done)

opensky (done)

## Contributing
DroneXtract is open to any contributions. Please fork the repository and make a pull request with the features or fixes you want to be implemented.

## Upcoming
- Get latest flown airports
- Get airport information
- latest flown aircraft
- get general avosint information
- get atc frequency info of airport
- enter identifier of aircraft or registration or tail number

## Support
If you enjoyed DroneXtract, please consider [becoming a sponsor](https://github.com/sponsors/ANG13T) in order to fund my future projects. 

To check out my other works, visit my [GitHub profile](https://github.com/ANG13T).


TODO:
- write README
- testing
- make cool banner and icon
- share on Linkedin, Reddit, GitHub, Twitter, and Discord