"""
Aircraft is a model describing the data retrieved about a specific aircraft
Fields include the following:

icao24 - 
"""

field_names = [
    "ICAO24",
    "Registration",
    "Manufacturer ICAO",
    "Manufacturer Name",
    "Model",
    "Type Code",
    "Serial Number",
    "Line Number",
    "ICAO Aircraft Type",
    "Operator",
    "Operator Callsign",
    "Operator ICAO",
    "Operator IATA",
    "Owner",
    "Test Registration",
    "Registered",
    "Registration Valid Until",
    "Status",
    "Built",
    "First Flight Date",
    "Seat Configuration",
    "Engines",
    "Modes",
    "ADSB",
    "ACARS",
    "Notes",
    "Category Description"
]


class Aircraft:
    def __init__(self, 
        tail_n, 
        msn=None, 
        call=None, 
        latitude=None, 
        longitude=None, 
        craft_type=None, 
        origin=None, 
        destination=None, 
        altitude=None, 
        manufacturer=None, 
        icao=None,
        notes=None
        ):

        self.tail_n         = tail_n
        self.msn            = msn
        self.call           = call
        self.origin         = origin
        self.manufacturer   = manufacturer
        self.destination    = destination
        self.altitude       = altitude	
        self.latitude       = latitude
        self.longitude      = longitude
        self.icao           = icao  
        self.notes          = notes


    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        obj = dir(self)
        output = ""
        for i in len(field_names):
            output += field_names[i] + ": " + obj[i] + " \n"
        return output
    
