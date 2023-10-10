from modules.opensky import get_opensky_data
from modules.wikipedia import get_wikipedia_data
from modules.aircraft import Aircraft

def osint_from_tail(tail_value):
    # 1. Get ICAO
    # 2. Get OpenSky
    # 3. Get Wikipedia
    aircraft = Aircraft()
    aircraft = get_opensky_data(aircraft, tail_value)
    aircraft = get_wikipedia_data(aircraft, tail_value)
    aircraft.print()
    return

def osint_from_icao(icao_value):
    return