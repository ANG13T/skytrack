## About
DroneXtract is a comprehensive digital forensics suite for DJI drones made with Golang. It can be used to analyze drone sensor values and telemetry data, visualize drone flight maps, audit for criminal activity, and extract pertinent data within multiple file formats. 

## Preview

<img alt="DroneXtract logo" width="600" src="https://github.com/ANG13T/DroneXtract/blob/main/assets/Preview.png">

## Information Gathered
- 
- 
-
-
-
- Much more!

## Features
DroneXtract features four main suites for drone forensics and auditing. They include the following:

### DJI File Parsing
You can visualize and extract information from DJI file formats such as CSV, KML, and GPX using the parsing tool.
The parsed information can be saved into an alternative file format when inputted an output file path.
The image below includes an example of a parsed file output and the type of data extracted from the file.

<img alt="DroneXtract logo" height="300" src="https://github.com/ANG13T/DroneXtract/blob/main/assets/demo-1.png">


### Steganography
Steganography refers to the process of revealing information stored within files.
The DroneXtract steganography suite allows you to extract telemetry and valuable data from image and video formats.
Additionally, the extracted data can be exported to four different file formats.

<img alt="DroneXtract logo" height="300" src="https://github.com/ANG13T/DroneXtract/blob/main/assets/demo-2.png">

### Tail Number (aka N-Number) to ICAO Converter
The telemetry visualization suite contains a flight path mapping generator and a telemetry graph visualizer.
The flight path mapping generator creates an image of a map indicating the locations the drone traveled to enroute and the path it took.
The telemetry graph visualizer plots a graph for each of the relevant telemetry or sensor values to be used for auditing purposes. 

<img alt="DroneXtract logo" width="600" src="https://github.com/ANG13T/DroneXtract/blob/main/assets/demo-3.png">

#### Disclaimer
Only works for United States aircraft registrations
The USA hex to ICAO tail number only works for USA registered aircraft

Use the following to learn about Aircraft registration numbers:
https://www.faa.gov/licenses_certificates/aircraft_certification/aircraft_registry/special_nnumbers

## Usage
To build from source, you will need Go installed.

```bash
$ export GO111MODULE=on
$ go get ./...
$ go run main.go
```

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

## Additional Info (What is ICAO? What is a Tail Number?)
Convert USA hex to ICAO

ICAO and Tail Numbers follow a mapping system like the following:

ICAO address	N-Number
a00001	N1
a00002	N1A
a00003	N1AA

## How does Conversion work?
ICAO Designations are represented by hexadecimal and have a fixed length of 6. This tool only supports U.S. ICAO designations which are denoted by the start letter 'a'. 

## Support
If you enjoyed DroneXtract, please consider [becoming a sponsor](https://github.com/sponsors/ANG13T) in order to fund my future projects. 

To check out my other works, visit my [GitHub profile](https://github.com/ANG13T).


TODO:
- write README
- testing
- make cool banner and icon
- share on Linkedin, Reddit, GitHub, Twitter, and Discord