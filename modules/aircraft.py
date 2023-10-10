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
    "Category Description",
    "Wiki Link"
]

class Aircraft:
    def __init__(self,
        icao24 = None,
        registration = None,
        manufacturer_icao = None,
        manufacturer_name = None,
        model = None,
        type_code = None,
        serial_number = None,
        line_number = None,
        icao_aircraft_type = None,
        operator = None,
        operator_callsign = None,
        operator_icao = None,
        operator_iata = None,
        owner = None,
        test_registration = None,
        registered = None,
        reg_valid_until = None,
        status = None,
        built = None,
        first_flight_date = None,
        seat_configuration = None,
        engines = None,
        modes = None,
        adsb = None,
        acars = None,
        notes = None,
        category_description = None,
        wiki_link = None
        ):
        self.ICAO24 = icao24
        self.Registration = registration
        self.Manufacturer_ICAO = manufacturer_icao
        self.Manufacturer_Name = manufacturer_name
        self.Model = model
        self.Type_Code = type_code
        self.Serial_Number = serial_number
        self.Line_Number = line_number
        self.ICAO_Aircraft_Type = icao_aircraft_type
        self.Operator = operator
        self.Operator_Callsign = operator_callsign
        self.Operator_ICAO = operator_icao
        self.Operator_IATA = operator_iata
        self.Owner = owner
        self.Test_Registration = test_registration
        self.Registered = registered
        self.Registration_Valid_Until = reg_valid_until
        self.Status = status
        self.Built = built
        self.First_Flight_Date = first_flight_date
        self.Seat_Configuration = seat_configuration
        self.Engines = engines
        self.Modes = modes
        self.ADSB = adsb
        self.ACARS = acars
        self.Notes = notes
        self.Category_Description = category_description
        self.Wiki_Link = wiki_link

    def print(self):
        obj = self.__dict__
        count = 0
        for key, value in obj.items():
            print(f"{field_names[count]}: {value}")
            count += 1


# class Aircraft:
#     def __init__(self, 
#         tail_n, 
#         msn=None, 
#         call=None, 
#         latitude=None, 
#         longitude=None, 
#         craft_type=None, 
#         origin=None, 
#         destination=None, 
#         altitude=None, 
#         manufacturer=None, 
#         icao=None,
#         notes=None
#         ):

#         self.tail_n         = tail_n
#         self.msn            = msn
#         self.call           = call
#         self.origin         = origin
#         self.manufacturer   = manufacturer
#         self.destination    = destination
#         self.altitude       = altitude	
#         self.latitude       = latitude
#         self.longitude      = longitude
#         self.icao           = icao  
#         self.notes          = notes


#     def __str__(self):
#         return self.__repr__()

#     def __repr__(self):
#         obj = dir(self)
#         output = ""
#         for i in len(field_names):
#             output += field_names[i] + ": " + obj[i] + " \n"
#         return output
    
