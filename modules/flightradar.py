from FlightRadar24 import FlightRadar24API
fr_api = FlightRadar24API()

"""
Information Derived from Flight Radar
Data Fields (number = 1)
Information about airports throughout the flight

- airport information departed and landed

"""

def get_flightradar_data():
    lukla_airport = fr_api.get_airport(code = "VNLK")
    print(lukla_airport)


