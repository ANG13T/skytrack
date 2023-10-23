"""
Aircraft is a model describing the data retrieved about a specific aircraft
Fields include the following:

icao24 - 
"""

from rich.align import Align
from rich.console import Console
from rich.live import Live
from rich.table import Table

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
    "Wiki Link",
    "Photos",
    "Flight History",
    "Flight Telemetry",
    "Registration Information",
    "Safety History",
    "Departure Airport",
    "Arrival Airport",
    "Departure METAR",
    "Arrival METAR"
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
        wiki_link = None,
        photos = None,
        history = None,
        telemetry = None,
        registration_details = None,
        safety_data = None,
        departure_airport = None,
        arrival_airport = None,
        departure_metar = None,
        arrival_metar = None
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
        self.photos = photos,
        self.history = history,
        self.telemetry = telemetry,
        self.registration_details = registration_details,
        self.safety_data = safety_data,
        self.departure_airport = departure_airport
        self.arrival_airport = arrival_airport
        self.departure_metar = departure_metar
        self.arrival_metar = arrival_metar
        

    def print(self):
        # allow option to see all flight history
        console = Console()
        table = Table(show_footer=False)
        table_centered = Align.left(table)
        obj = self.__dict__

        with Live(table_centered, console=console,
          screen=False):
            print(self.arrival_metar, len(obj.items()))
            table.add_column(f"Aircraft Information for {self.Registration}", no_wrap=True)
            count = 0
            for key, value in obj.items():
                print(key, value, len(value))
                if len(value) > 0:
                    table.add_row(f"[b white]{field_names[count]}[/]: [white]{value} [/]")
                count += 1
        
            table_width = console.measure(table).maximum
        
            table.width = None
        console.print(table)