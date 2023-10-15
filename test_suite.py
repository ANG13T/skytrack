from modules.jet_photos import get_jetphotos_data
from modules.flight_aware import get_flightaware_data, get_airport_code, get_airport_name

print(get_jetphotos_data("N450FE"))
print(get_airport_code(get_flightaware_data("N195PS")["departure"]))
print(get_airport_name(get_flightaware_data("N195PS")["arrival"]))