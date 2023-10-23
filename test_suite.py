from modules.jet_photos import get_jetphotos_data
from modules.flight_aware import get_flightaware_data, get_airport_code, get_airport_name
from modules.airport_info import get_airport_info
from modules.metar import get_metar_data

print(get_jetphotos_data("N450FE"))
flight_aware_data = get_flightaware_data("N137RJ")
aiport_code = get_airport_code(flight_aware_data["arrival"])
airport_name = get_airport_name(flight_aware_data["arrival"])
print("AAA", flight_aware_data["telemetry"].arrival_time, "AAA", aiport_code, airport_name)
airport_info = get_airport_info(aiport_code, airport_name)
print(airport_info.ident, flight_aware_data["telemetry"].arrival_time)

print(aiport_code, get_metar_data(airport_info.ident, flight_aware_data["telemetry"].arrival_time))
# print(flight_aware_data["telemetry"].departure_time, get_metar_data(get_airport_info(flight_aware_data["departure"]).ident), get_airport_info(flight_aware_data["departure"]))
# print(get_metar_data(get_airport_info(flight_aware_data["departure"]).ident, flight_aware_data["telemetry"].departure_time))