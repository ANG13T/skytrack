from time import sleep
from modules.icao_tail import *
from modules.option import generate_option
from rich.console import Console
from modules.menu import rerun
import os

console = Console()

try: 
    def run_icao_tail():
        options = [
            "🛫  Convert Tail Number to ICAO Designator",
            "🛬  Convert ICAO Designator to Tail Number",
            "Back to Main Menu"
        ]

        option = generate_option(options)

        if option == 1:
            value = console.input("Enter [bold blue]Tail Number[/]: ")
            print_tail_to_icao(value)
            
        if option == 2:
            value = console.input("Enter [bold blue]ICAO Designation[/]: ")
            print_icao_to_tail(value)
        
    run_icao_tail()

except KeyboardInterrupt:
    print("\n")
    console.print("[bold][cyan] Exiting skytrack [/cyan][/bold]")
    sleep(1)

except TypeError:
    os.system("clear")
    print("hi 4")
    rerun()