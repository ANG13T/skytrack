from modules.jet_photos import get_jetphotos_data
from modules.flightradar import get_flightradar_data
from modules.flight_aware import get_flightaware_data

print(get_jetphotos_data("N450FE"))
get_flightradar_data()
get_flightaware_data("N195PS")