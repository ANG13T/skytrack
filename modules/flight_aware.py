import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import re

"""
Information Derived from Flight Aware
Data Fields (number = 3)
- Flight History and Latest Flight (done)
- Flight Track Log and Telemetry (log it on a chart)
- Regsitration Information

https://www.flightaware.com/live/flight/N195PS/history/20231003/1950Z/KSMO/KEMT/tracklog

https://www.flightaware.com/live/flight/N195PS

https://www.flightaware.com/resources/registration/N195PS
"""

BASE_URL = "https://www.flightaware.com"
URL = "https://www.flightaware.com/live/flight/"

def get_flightaware_data(tail_value):
    updated_url = URL + tail_value
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
    driver.quit()

    soup = BeautifulSoup(history_page, "html.parser")


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
