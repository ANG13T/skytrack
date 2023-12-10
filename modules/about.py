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
        console.print("The purpose of skytrack is to provide accurate and holistic OSINT platform for aircraft using lots of reliable data sources. It is able to gather data such as aircraft model, type, operator, telemetry, and much more.")

        console.print("\n[bold underline cyan]skytrack Utilities[/]\n")
        console.print("🛫  [bold]Extract Information about a Plane[/]\n")
        console.print("Retrieve general aircraft information and flight history logs. You can select the plane by specifying its tail number or ICAO designator.")
        console.print("\n📘  [bold]Generate Flight Information PDF[/]\n")
        console.print("Save the retrieved aircraft information into a PDF for later reference.")
        console.print("\n🛬  [bold]Tail Number and ICAO Conversion[/]\n")
        console.print("Convert an aircraft tail number specification to an ICAO designator and vice versa.")

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