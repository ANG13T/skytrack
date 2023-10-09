from simple_term_menu import TerminalMenu
from time import sleep
from modules.icao_tail import *
from rich.console import Console
from modules.menu import rerun
import os

console = Console()

try: 
    def run_icao_tail():
        run_icao_tail.options = [
            "🛫  Input Tail Number",
            None,
            "🛬  Input ICAO Designator",
            None,
            "Back to Main Menu"
        ]
        run_icao_tail.terminal_menu = TerminalMenu(
            run_icao_tail.options,
            title="",
            menu_cursor=" ❯ ",
            menu_cursor_style=("fg_blue", "bold"),
            menu_highlight_style=("fg_cyan", "underline", "bold"),
        )
        run_icao_tail.menu_entry_index = run_icao_tail.terminal_menu.show() / 2
        if run_icao_tail.menu_entry_index == 0:
            value = console.input("Enter [bold blue]Tail Number[/]: ")
            print_tail_to_icao(value)
            
        if run_icao_tail.menu_entry_index == 1:
            value = console.input("Enter [bold blue]ICAO Designation[/]: ")
            print_icao_to_tail(value)
        
    run_icao_tail()

except KeyboardInterrupt:
    print("\n")
    console.print("[bold][cyan] Exiting skytrack [/cyan][/bold]")
    sleep(1)

except TypeError:
    os.system("clear")
    rerun()