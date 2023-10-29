from time import sleep
from modules.icao_tail import *
from modules.osint import *
from modules.option import generate_option
from rich.console import Console
from modules.menu import rerun
import os

console = Console()

try: 
    def osint_options_menu():
        osint_options_menu.options = [
            "🛫  Input Tail Number",
            "🛬  Input ICAO Designator",
            "Back to Main Menu"
        ]
        
        option = generate_option(osint_options_menu.options)

        if option == 1:
            value = console.input("Enter [bold blue]Tail Number[/]: ")
            osint_from_tail(value)

        if option == 2:
            value = console.input("Enter [bold blue]ICAO Designation[/]: ")
            osint_from_icao(value)
        
    osint_options_menu()

except KeyboardInterrupt:
    print("\n")
    console.print("[bold][cyan] Exiting skytrack [/cyan][/bold]")
    sleep(1)

except TypeError:
    #os.system("clear")
    rerun()