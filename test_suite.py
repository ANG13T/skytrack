from modules.jet_photos import get_jetphotos_data
from modules.flight_aware import get_flightaware_data, get_airport_code, get_airport_name
from modules.airport_info import get_airport_info

print(get_jetphotos_data("N450FE"))
flight_aware_data = get_flightaware_data("N137RJ")
# aiport_code = get_airport_code(["arrival"])
# airport_name = get_airport_name(get_flightaware_data("N137RJ")["arrival"])
# print(get_flightaware_data("N137RJ")["arrival"])