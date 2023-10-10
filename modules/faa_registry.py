"""
Information extracted from https://registry.faa.gov/AircraftInquiry
Data Fields (number = )

Aircraft Description
=====================

Serial Number: String - Aircraft registration number.

Manufacturer Name: String - Aircraft registration number.

Type Aircraft: String - Aircraft registration number.

Pending Number Change

Date Change Authorized

MFR Year

Type Registration

Registered Owner
=====================

Name

Street

City

County

Country

Airworthiness
=====================

Type Certificate Data Sheet

Engine Manufacturer

Engine Model

A/W Date

Temporary Certificates
=======================

Fuel Modifications
=====================


* Checks if values are blank

Example: https://registry.faa.gov/AircraftInquiry/Search/NNumberResult (N1181A)

"https://registry.faa.gov/AircraftInquiry/Search/NNumberResult?nNumberTxt="+tail_n
"""

