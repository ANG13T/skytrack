import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

"""
Information Derived from Flight Aware
Data Fields (number = 1)
- Flight Data (Distance)
- Latest Flight (airports, distance, etc)
- Flight History
- Flight Track Log and Telemetry (log it on a chart)

https://www.flightaware.com/live/flight/N195PS/history/20231003/1950Z/KSMO/KEMT/tracklog

https://www.flightaware.com/live/flight/N195PS


"""

BASE_URL = "https://www.flightaware.com"
URL = "https://www.flightaware.com/live/flight/"

def get_flightaware_data(tail_value):
    updated_url = URL + tail_value
    driver = webdriver.Firefox()
    driver.get(updated_url)
    time.sleep(3)
    page = driver.page_source
    driver.quit()
    soup = BeautifulSoup(page, "html.parser")
    items = soup.find_all("a") #  TODO: optimize

    # Get Link for History

    flight_history_url = ""

    for item in items:
        if "View track log" in str(item):
            flight_history_url = BASE_URL + item["href"]
    if flight_history_url == "":
        return None
    print(flight_history_url)
