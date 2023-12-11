"""
Aircraft is a model describing the data retrieved about a specific aircraft
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
                 icao24=None,
                 registration=None,
                 manufacturer_icao=None,
                 manufacturer_name=None,
                 model=None,
                 type_code=None,
                 serial_number=None,
                 line_number=None,
                 icao_aircraft_type=None,
                 operator=None,
                 operator_callsign=None,
                 operator_icao=None,
                 operator_iata=None,
                 owner=None,
                 test_registration=None,
                 registered=None,
                 reg_valid_until=None,
                 status=None,
                 built=None,
                 first_flight_date=None,
                 seat_configuration=None,
                 engines=None,
                 modes=None,
                 adsb=None,
                 acars=None,
                 notes=None,
                 category_description=None,
                 wiki_link=None,
                 photos=None,
                 history=None,
                 telemetry=None,
                 registration_details=None,
                 safety_data=None,
                 departure_airport=None,
                 arrival_airport=None,
                 departure_metar=None,
                 arrival_metar=None
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
        self.Photos = photos,
        self.History = history,
        self.Telemetry = telemetry,
        self.Registration_Details = registration_details,
        self.Safety_Data = safety_data,
        self.Departure_Airport = departure_airport
        self.Arrival_Airport = arrival_airport
        self.Departure_Metar = departure_metar
        self.Arrival_Metar = arrival_metar

    def get_row_content(self, key, value):
        if (not value == None) and len(value) > 0:
            content = value
            if str(value) == "false":
                content = "Not Included"
            elif str(value) == "true":
                content = "Included"
            return f"[b white]{key}[/]: [blue]{content} [/]"
        else:
            return ""

    def get_flight_history(self, history):
        if history == None or len(history) == 0:
            return None
        return history

    def get_flight_photos(self, photos):
        if photos == None or len(photos) == 0:
            return None

        if len(photos) > 1:
            return "\n" + "\n".join(photos)
        else:
            return "\n" + photos[0]

    def parse_flight_log(self, log):
        date = log[0]
        duration = ":".join(log[-2:])
        aircraft = log[-3]
        airports_info = log[1:len(log) - 3]
        departure = " ".join(airports_info[:6])
        arrival = " ".join(airports_info[6:])
        return [date, departure, arrival, aircraft, duration]
    
    def parsed_flight_history(self):
        hist = []
        for log in self.History:
            hist.append(self.parse_flight_log(log))
        return hist

    def print_flight_history(self, history):
        table_title = f"Flight History for {self.Registration} ✈️"
        table = Table(title=table_title, show_footer=False)
        table_centered = Align.left(table)
        console =  Console()

        with Live(table_centered, console=console,
                screen=False):
            table.add_column(
                "Date", no_wrap=True)
            table.add_column(
                "Departure", no_wrap=True)
            table.add_column(
                "Arrival", no_wrap=True)
            table.add_column(
                "Aircraft", no_wrap=True)
            table.add_column(
                "Duration", no_wrap=True)

            for log in history:
                if log and len(log) > 0:
                    log = self.parse_flight_log(log)
                    if len(log) == 5:
                        table.add_row(log[0], log[1], log[2], log[3], log[4])

            table.width = None

        console.print("\n")


    def print(self):
        # allow option to see all flight history
        console = Console()
        table = Table(show_footer=False)
        table_centered = Align.left(table)

        contents = []

        contents.append(self.get_row_content("ICAO24", self.ICAO24))
        contents.append(self.get_row_content(
            "Registration", self.Registration))
        contents.append(self.get_row_content(
            "Manufacturer ICAO", self.Manufacturer_ICAO))
        contents.append(self.get_row_content(
            "Manufacturer Name", self.Manufacturer_Name))
        contents.append(self.get_row_content("Model", self.Model))
        contents.append(self.get_row_content("Type Code", self.Type_Code))
        contents.append(self.get_row_content(
            "Serial Number", self.Serial_Number))
        contents.append(self.get_row_content("Line Number", self.Line_Number))
        contents.append(self.get_row_content(
            "ICAO Aircraft Type", self.ICAO_Aircraft_Type))
        contents.append(self.get_row_content("Operator", self.Operator))
        contents.append(self.get_row_content(
            "Operator Callsign", self.Operator_Callsign))
        contents.append(self.get_row_content(
            "Operator ICAO", self.Operator_ICAO))
        contents.append(self.get_row_content(
            "Operator IATA", self.Operator_IATA))
        contents.append(self.get_row_content("Owner", self.Owner))
        contents.append(self.get_row_content(
            "Test Registration", self.Test_Registration))
        contents.append(self.get_row_content("Registered", self.Registered))
        contents.append(self.get_row_content(
            "Registration Valid Until", self.Registration_Valid_Until))
        contents.append(self.get_row_content("Status", self.Status))
        contents.append(self.get_row_content("Built", self.Built))
        contents.append(self.get_row_content(
            "First Flight Date", self.First_Flight_Date))
        contents.append(self.get_row_content(
            "Seat Configuration", self.Seat_Configuration))
        contents.append(self.get_row_content("Engines", self.Engines))
        contents.append(self.get_row_content("Modes", self.Modes))
        contents.append(self.get_row_content("ADSB", self.ADSB))
        contents.append(self.get_row_content("ACARS", self.ACARS))
        contents.append(self.get_row_content("Notes", self.Notes))
        contents.append(self.get_row_content(
            "Category Description", self.Category_Description))
        contents.append(self.get_row_content("Wiki Link", self.Wiki_Link))
        contents.append(self.get_row_content(
            "Photos", self.get_flight_photos(self.Photos)))
        
        with Live(table_centered, console=console,
                  screen=False):
            table.add_column(
                f"Aircraft Information for {self.Registration} ✈️", no_wrap=True)

            for content in contents:
                if len(content) > 0:
                    table.add_row(content)

            table.width = None

        console.print("\n")

        self.print_flight_history(self.History)
