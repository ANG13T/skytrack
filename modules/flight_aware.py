import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import re

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
    print(parse_past_flights(words))
    # if past_flights != None:
    #     past_flight_children = past_flights.findChildren()
    #     for child in past_flight_children:
    #         if child.contains
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

    print(parse_flight_telemetry(flight_logs))

    soup = BeautifulSoup(registration_url, "html.parser")

    title_1 = soup.find_all("div", {"class": "medium-1"})
    subtitle = soup.find_all("div", {"class": "medium-3"})
    history_table = soup.find_all("div", {"class": "airportBoardContainer"})

    parse_registration_information(title_1, subtitle, history_table)


    # Get Link for History
    print(flight_history_url)

# TODO: make a past flight model
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
    return result


def parse_flight_telemetry(logs):
    result = []
    marker = -1
    tracker = -1
    for log in logs:
        if "PM" in log:
            result.append([])
            marker += 1
            result[marker].append(log)
            tracker = 1
        elif tracker != -1 and tracker < 8:
            result[marker].append(log)
            tracker += 1
    final = []
    for res in result:
        if len(res) == 8:
            final.append(res)
    return final

def parse_registration_information(titles, subtitles, table):
    table = table[0].text.strip()
    table = re.split(r'\s+', table)
    parsed_contents = []
    table_contents = []
    for index in range(len(titles)):
        parsed_contents.append([])
        parsed_contents[index] = titles[index].text.strip()
        parsed_contents[index] = subtitles[index].text.strip()
    print(table)
    map = -1
    for item in table:
        if item != "Date" and item != "Owner" and item != "Location":
            if "Date" in item:
                table_contents.append([])
                map += 1
                table_contents[map].append(item)
            elif map > -1:
                table_contents[map].append(item)
    print(table_contents)