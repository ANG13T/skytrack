from modules.opensky import get_opensky_data
from modules.wikipedia import get_wikipedia_data
from modules.jet_photos import get_jetphotos_data
from modules.models.aircraft import Aircraft

def osint_from_tail(tail_value):
    # 1. Get ICAO
    # 2. Get OpenSky
    # 3. Get Wikipedia
    # 4. Get Photos from Jet Photos
    aircraft = Aircraft()
    aircraft = get_opensky_data(aircraft, tail_value)
    aircraft = get_wikipedia_data(aircraft, tail_value)
    aircraft.photos = get_jetphotos_data(tail_value)
    aircraft.print()
    return

def osint_from_icao(icao_value):
    return