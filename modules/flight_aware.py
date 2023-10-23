import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import re
from modules.models.flight_registration import FlightRegistration
from modules.models.flight_history import FlightHistory
from modules.models.flight_telemetry import FlightTelemetry
import dateparser
import datetime as DT

"""
Information Derived from Flight Aware
Data Fields (number = 3)
- Flight History and Latest Flight
- Flight Track Log and Telemetry (log it on a chart)
- Regsitration Information

Example URLS:
https://www.flightaware.com/live/flight/N195PS/history/20231003/1950Z/KSMO/KEMT/tracklog

https://www.flightaware.com/live/flight/N195PS

https://www.flightaware.com/resources/registration/N195PS
"""

# Get Aiport TO and FROM INFO

BASE_URL = "https://www.flightaware.com"
URL = "https://www.flightaware.com/live/flight/"
REGISTRATION_URL = "https://www.flightaware.com/resources/registration/"

def get_flightaware_data(tail_value):
    updated_url = URL + tail_value
    registration_tail_url = REGISTRATION_URL + tail_value
    driver = webdriver.Firefox()
    driver.get(updated_url)
    time.sleep(3)
    page = driver.page_source

    soup = BeautifulSoup(page, "html.parser")

    past_flights = soup.find(id="flightPageActivityLog").text.strip()
    words = re.split(r'\s+', past_flights)
    history = parse_past_flights(words)
    items = soup.find_all("a") #  TODO: optimize

    for item in items:
        if "View track log" in str(item):
            flight_history_url = BASE_URL + item["href"]
    if flight_history_url == "":
        return None

    driver.get(flight_history_url)
    time.sleep(5)
    history_page = driver.page_source

    driver.get(registration_tail_url)
    time.sleep(5)
    registration_url = driver.page_source
    driver.quit()

    soup = BeautifulSoup(history_page, "html.parser")

    flight_logs = soup.find(id="tracklogTable").text.strip()
    flight_logs = re.split(r'\s+', flight_logs)

    arrival_data = get_arrival_airport(history)
    departure_data = get_departure_airport(history)

    telem = parse_flight_telemetry(flight_logs, arrival_data, departure_data)

    soup = BeautifulSoup(registration_url, "html.parser")

    title_1 = soup.find_all("div", {"class": "medium-1"})
    subtitle = soup.find_all("div", {"class": "medium-3"})
    history_table = soup.find_all("div", {"class": "airportBoardContainer"})

    registration = parse_registration_information(title_1, subtitle, history_table)

    return {"history": history, "telemetry": telem, "registration": registration, "arrival": arrival_data, "departure": departure_data}

def parse_past_flights(flights):
    result = []
    marker = -1
    for flight in flights:
        if flight == "Join":
            return result
        if len(flight.split("-")) > 2:
            result.append([])
            marker += 1
            result[marker].append(flight)
        elif len(result) > 0:
            result[marker].append(flight)
    return FlightHistory(result)

def get_departure_airport(history):
        if len(history) == 0:
            return None
        return history[0]

def get_arrival_airport(history):
        if len(history) == 0:
            return None
        return history[len(history) - 1]

def parse_flight_telemetry(logs, arrival_data, departure_data):
    result = []
    output = FlightTelemetry([])
    marker = -1
    tracker = -1
    for index, log in enumerate(logs):
        if "PM" in log:
            result.append([])
            marker += 1
            result[marker].append(log)
            tracker = 1
        elif tracker != -1 and tracker < 8:
            result[marker].append(log)

            if "Departure" in log:
                output.departure_time = parse_time([departure_data[0]] + logs[index + 4: index + 7])

            elif "Arrival" in log:
                print(logs[index: index + 10])
                output.arrival_time = parse_time([arrival_data[0]] + logs[index + 4: index + 7])

            tracker += 1
    final = []
    for res in result:
        if len(res) == 8:
            final.append(res)
    output.telemetry = final
    return output

def parse_time(time_array):
    print("timing", time_array)
    output = dateparser.parse(" ".join(time_array))
    output = output.astimezone(DT.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    print("results", " ".join(time_array), "monkey", output)
    return output

def parse_registration_information(titles, subtitles, table):
    table = table[0].text.strip()
    table = re.split(r'\s+', table)
    parsed_contents = []
    table_contents = []
    for index in range(len(titles)):
        parsed_contents.append([])
        parsed_contents[index] = titles[index].text.strip()
        parsed_contents[index] = subtitles[index].text.strip()
    map = -1
    for item in table:
        if item != "Date" and item != "Owner" and item != "Location":
            if "Date" in item:
                table_contents.append([])
                map += 1
                table_contents[map].append(item)
            elif map > -1:
                table_contents[map].append(item)
    return FlightRegistration(parsed_contents, table_contents)


def get_airport_code(airport):
    if airport == None:
        return None
    for index, value in enumerate(airport):
        if value == "-":
            return airport[index + 1]
    return None

def get_airport_name(airport):
    if airport == None:
        return None
    for index, value in enumerate(airport):
        if len(value) == 3:
            return airport[index + 1]
    return None