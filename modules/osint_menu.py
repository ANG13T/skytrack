from time import sleep
from modules.icao_tail import *
from modules.osint import *
from modules.option import generate_option
from rich.console import Console
from modules.menu import rerun
import os

console = Console()

try: 
    def run_icao_tail():
        run_icao_tail.options = [
            "🛫  Input Tail Number",
            "🛬  Input ICAO Designator",
            "Back to Main Menu"
        ]
        
        option = generate_option(run_icao_tail.options)

        if option == 0:
            value = console.input("Enter [bold blue]Tail Number[/]: ")
            osint_from_tail(value)
            
        if option == 1:
            value = console.input("Enter [bold blue]ICAO Designation[/]: ")
            osint_from_icao(value)
        
    run_icao_tail()

except KeyboardInterrupt:
    print("\n")
    console.print("[bold][cyan] Exiting skytrack [/cyan][/bold]")
    sleep(1)

except TypeError:
    os.system("clear")
    rerun()