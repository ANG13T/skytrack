from time import sleep
from modules.option import generate_option
from rich.console import Console
from modules.menu import rerun

try: 
    def about_options_menu():
        about_options_menu.options = [
            "Back to Main Menu"
        ]

        console = Console()

        console.print("\n[bold underline cyan]About skytrack[/]\n")
        console.print("skytrack is an aviation CLI tool written with Python that gathers a wide breadth of data about a specific aircraft given its tail number or ICAO designator")

        console.print("\n[bold underline cyan]skytrack Purpose[/]\n")
        console.print("The purpose of skytrack is to provide accurate and holistic OSINT platform for aircraft. It is able to gather data such as aircraft model, type, operator, telemetry, and much more.")

        console.print("\n[bold underline cyan]skytrack Utilities[/]\n")
        console.print("🌦  [bold]Weather Forecasts and Alerts[/]\n")
        console.print("Get up-to-date weather forecasts, data, and alerts from NOAA satellites. You can choose to get information via GPS coordinates, station ID, or area code")
        console.print("\n🛰  [bold]Pass Predictor[/]\n")
        console.print("Predict for radio or visual satellite passes of all NOAA satellites by inputting your GPS coordinates")
        console.print("\n📡  [bold]APT Image Decoder[/]\n")
        console.print("Decode NOAA satellite images by inputting audio MP3 files of satellite transmissions.")
        console.print("\n🌎  [bold]Meteorological Image Analysis[/]\n")
        console.print("Retrieve meteorological images from the Sentinel-2 data collection for remote sensing analysis.")

        console.print("\n[bold underline cyan]About the Developer[/]\n")
        console.print("skytrack was created by Angelina Tsuboi (G4LXY). To get in touch with me, you can reach out via the following methods:\n")
        console.print("[bold]Website:[/] angelinatsuboi.com")
        console.print("[bold]Instagram:[/] @angelina_tsuboi")
        console.print("[bold]Twitter:[/] @AngelinaTsuboi")
        console.print("[bold]GitHub:[/] @ANG13T")

        console.print("\n[bold underline cyan]Contributing and Support[/]\n")
        console.print("All contributions to this tool are welcome. Please refer the contribution guideline on skytrack's GitHub repository to submit a pull request.")
        console.print("To support my work and future projects, please consider sponsoring me on GitHub:")
        console.print("https://github.com/sponsors/ANG13T")
        console.print("\n[bold]Skytrack GitHub Repo:[/]")
        console.print("https://github.com/ANG13T/skytrack \n")
        
        option = generate_option(about_options_menu.options)
        
    about_options_menu()

except KeyboardInterrupt:
    print("\n")
    console.print("[bold][cyan] Exiting skytrack [/cyan][/bold]")
    sleep(1)

except TypeError:
    #os.system("clear")
    rerun()