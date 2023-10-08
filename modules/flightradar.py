from FlightRadar24 import FlightRadar24API
fr_api = FlightRadar24API()

airline_icao = "UAE"
aircraft_type = "B77W"

zone = fr_api.get_zones()["northamerica"]
bounds = fr_api.get_bounds(zone)

emirates_flights = fr_api.get_flights(
    aircraft_type = aircraft_type,
    airline = airline_icao,
    bounds = bounds
)


