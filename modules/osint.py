from modules.opensky import get_opensky_data

def osint_from_tail(tail_value):
    information = get_opensky_data(tail_value)
    print(information)
    return

def osint_from_icao(icao_value):
    return