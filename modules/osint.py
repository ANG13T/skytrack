from modules.opensky import get_opensky_data
from modules.wikipedia import get_wikipedia_data
from modules.jet_photos import get_jetphotos_data
from modules.flight_aware import get_flightaware_data, get_airport_code, get_airport_name
from modules.aviation_safety import get_aviation_safety_data
from modules.airport_info import get_airport_info
from modules.metar import get_metar_data
from modules.models.aircraft import Aircraft
from rich.console import Console
from modules.icao_tail import icao_to_tail, tail_to_icao

import jinja2
import pandas as pd
from xhtml2pdf import pisa

console = Console()


def osint_from_tail(tail_value, pdf=False):
    # 1. Get ICAO
    # 2. Get OpenSky
    # 3. Get Wikipedia
    # 4. Get Photos from Jet Photos
    # 5. Get Data from Flight Aware (TODO: ask for permission to use emulation)
    # 6. Get Airport Information
    # 7. Get METAR Information for both Arrival and Departure Airports
    with console.status("[white]Fetching data...[/white]") as status:
        icao = tail_to_icao(tail_value)
        if not icao == None:
            icao == icao.upper()
        else:
            return

        aircraft = Aircraft(registration=tail_value, icao24=icao)
        console.log("[blue]✈️  Fetching OpenSky Data[/blue]")
        aircraft = get_opensky_data(aircraft, tail_value)
        console.log("[green]✓ Finish Fetching OpenSky Data[/green]")
        console.log("[blue]✈️  Fetching Wikipedia Data[/blue]")
        aircraft = get_wikipedia_data(aircraft, tail_value)
        console.log("[green]✓ Finish Fetching Wikipedia Data[/green]")
        console.log("[blue]✈️  Fetching Jet Photos Data[/blue]")
        aircraft.Photos = get_jetphotos_data(tail_value)
        console.log("[green]✓ Finish Fetching Jet Photos Data[/green]")
        console.log("[blue]✈️  Fetching FlightAware Data[/blue]")
        flight_aware = get_flightaware_data(tail_value)
        aircraft.History = flight_aware["history"]
        aircraft.Telemetry = flight_aware["telemetry"]
        aircraft.Registration_Details = flight_aware["registration"]
        console.log("[green]✓ Finish Fetching FlightAware Data[/green]")
        console.log("[blue]✈️  Fetching Aviation Safety Data[/blue]")
        aircraft.Safety_Data = get_aviation_safety_data(tail_value)
        console.log("[green]✓ Finish Fetching Aviation Safety Data[/green]")
        console.log("[blue]✈️  Fetching Airport Data[/blue]")
        d_aiport_code = get_airport_code(flight_aware["departure"])
        d_airport_name = get_airport_name(flight_aware["departure"])
        a_aiport_code = get_airport_code(flight_aware["arrival"])
        a_airport_name = get_airport_name(flight_aware["arrival"])
        aircraft.Departure_Airport = get_airport_info(
            d_aiport_code, d_airport_name)
        aircraft.Arrival_Airport = get_airport_info(
            a_aiport_code, a_airport_name)
        if aircraft.Arrival_Airport:
            aircraft.Arrival_Metar = get_metar_data(
                aircraft.Arrival_Airport.ident, aircraft.Telemetry.arrival_time)
        if aircraft.Departure_Metar:
            aircraft.Departure_Metar = get_metar_data(
                aircraft.Departure_Airport.ident, aircraft.Telemetry.departure_time)
    console.log("[green]Finish Fetching Airport Data[/green]")
    aircraft.print()

    if pdf == True:
        html = jinja2.Environment(  
        loader=jinja2.FileSystemLoader(searchpath='templates')).get_template(
            'osint_report.html').render(aircraft=aircraft)

        with open('report.pdf', "w+b") as out_pdf_file_handle:
            pisa.CreatePDF(
                src=html, 
                dest=out_pdf_file_handle)


def osint_from_icao(icao_value, pdf = False):
    osint_from_tail(icao_to_tail(icao_value), pdf)
