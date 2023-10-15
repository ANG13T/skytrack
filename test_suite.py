from modules.jet_photos import get_jetphotos_data
from modules.flight_aware import get_flightaware_data, get_airport_code, get_airport_name
from modules.airport_info import get_airport_info

print(get_jetphotos_data("N450FE"))
aiport_code = get_airport_code(get_flightaware_data("N195PS")["departure"])
airport_name = get_airport_name(get_flightaware_data("N195PS")["arrival"])
print(get_airport_info(aiport_code, airport_name))