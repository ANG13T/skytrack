<img alt="skytrack banner" width="700" src="https://github.com/ANG13T/skytrack/blob/main/assets/data/skytrack_banner.png">

## About
skytrack is a command-line based plane spotting and aircraft OSINT reconnaissance tool made using Python.
It can gather aircraft information using various data sources, generate a PDF report for a specified aircraft, and convert between ICAO and Tail Number designations. 
Whether you are a hobbyist plane spotter or an experienced aircraft analyst, skytrack can help you identify and enumerate aircraft for general purpose reconnaissance.

## What is Planespotting & Aircraft OSINT?
Planespotting is the art of tracking down and observing aircraft. While planespotting mostly consists of photography and videography of aircraft, aircraft information gathering and OSINT is a crucial step in the planespotting process. OSINT (Open Source Intelligence) describes a methodology of using publicy accessible data sources to obtain data about a specific subject — in this case planes! 

## Aircraft Information 
- Tail Number 🛫
- Aircraft Type ⚙️
- ICAO24 Designation 🔎
- Manufacturer Details 🛠
- Flight Logs 📄 
- Aircraft Owner ✈️
- Model 🛩
- Much more!

## Usage
To run skytrack on your machine, follow the steps below:

```bash
$ git clone https://github.com/ANG13T/skytrack
$ cd skytrack
$ pip install -r requirements.txt
$ python skytrack.py
```

skytrack works best for Python version 3.

## Preview

<img alt="skytrack preview" width="500" src="https://github.com/ANG13T/skytrack/blob/main/assets/data/skytrack_preview.png">

## Features
skytrack features three main functions for aircraft information gathering and display options. They include the following:

### Aircraft Reconnaissance & OSINT
skytrack obtains general information about the aircraft given its tail number or ICAO designator.
The tool sources this information using several reliable data sets.
Once the data is collected, it is displayed in the terminal within a table layout.

<img alt="skytrack display" height="300" src="https://github.com/ANG13T/skytrack/blob/main/assets/data/display_1.png"> 

### PDF Aircraft Information Report
skytrack also enables you the save the collected aircraft information into a PDF.
The PDF includes all the aircraft data in a visual layout for later reference.
The PDF report will be entitled "skytrack_report.pdf"

<img alt="skytrack display" height="300" src="https://github.com/ANG13T/skytrack/blob/main/assets/data/display_2.png">

### Tail Number to ICAO Converter
There are two standard identification formats for specifying aircraft: Tail Number and ICAO Designation. The tail number (aka N-Number) is an alphanumerical ID starting with the letter "N" used to identify aircraft. The ICAO type designation is a six-character fixed-length ID in the hexadecimal format. 
Both standards are highly pertinent for aircraft reconnaissance as they both can be used to search for a specific aircraft in data sources.
However, converting them from one format to another can be rather cumbersome as it follows a tricky algorithm. To streamline this process, skytrack includes a standard converter. 

<img alt="skytrack display" height="150" src="https://github.com/ANG13T/skytrack/blob/main/assets/data/display_3.png">

<details>
<summary><bold>Further Explanation</bold></summary>

<br />

<p>ICAO and Tail Numbers follow a mapping system like the following:</p>

<p>ICAO address	N-Number (Tail Number)</p>
<p>a00001	        N1</p>
<p>a00002	        N1A</p>
<p>a00003	        N1AA</p>

You can learn more about aircraft registration numbers [here](https://www.faa.gov/licenses_certificates/aircraft_certification/aircraft_registry/special_nnumbers)

</details>

> :warning:  Converter only works for USA-registered aircraft

## Data Sources & APIs Used
[ICAO Aircraft Type Designators Listings](https://www.icao.int/publications/doc8643/pages/search.aspx)

[FlightAware](flightaware.com)

[Wikipedia](wikipedia.org)

[Aviation Safety Website](https://aviation-safety.net)

[Jet Photos Website](https://www.jetphotos.com)

[OpenSky API](https://opensky-network.org/datasets/metadata/aircraftDatabase.csv)

[Aviation Weather METAR](https://aviationweather.gov)

[Airport Codes Dataset](https://pkgstore.datahub.io/core/airport-codes/airport-codes/archive/dfadb79d7ba34a49242332f2eaf4f1b0/airport-codes.csv)

## Contributing
skytrack is open to any contributions. Please fork the repository and make a pull request with the features or fixes you want to implement.

## Upcoming
- Obtain Latest Flown Airports
- Obtain Airport Information
- Obtain ATC Frequency Information

## Support
If you enjoyed skytrack, please consider [becoming a sponsor](https://github.com/sponsors/ANG13T) or donating on [buymeacoffee](https://www.buymeacoffee.com/angelinatsuboi) in order to fund my future projects. 

To check out my other works, visit my [GitHub profile](https://github.com/ANG13T).
