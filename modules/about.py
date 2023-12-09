from time import sleep
from modules.icao_tail import *
from modules.osint import *
from modules.option import generate_option
from rich.console import Console
from modules.menu import rerun
import os

console = Console()

try: 
    def about_options_menu():
        about_options_menu.options = [
            "Back to Main Menu"
        ]
        
        option = generate_option(about_options_menu.options)

        print("About this tool")
        
    about_options_menu()

except KeyboardInterrupt:
    print("\n")
    console.print("[bold][cyan] Exiting skytrack [/cyan][/bold]")
    sleep(1)

except TypeError:
    #os.system("clear")
    rerun()