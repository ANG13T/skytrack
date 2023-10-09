from modules import *
from time import sleep
from simple_term_menu import TerminalMenu
from modules.rerun import rerun
# from modules.about import about
from rich.console import Console
from modules.banner import *
import os

console = Console()

try:
    main_banner()

    def menu():
        menu.options = [
            "🛫 Extract Information about Plane",
            None,
            "📘 Generate Flight Information PDF",
            None,
            "🛬 Tail Number and ICAO Conversion",
            None,
            "ℹ️  About and Usage",
            None,
            "Exit skytrack",
        ]

        terminal_menu = TerminalMenu(
            menu.options,
            title="",
            menu_cursor=" ❯ ",
            menu_cursor_style=("fg_blue", "bold"),
            menu_highlight_style=("fg_cyan", "underline", "bold"),
            skip_empty_entries=True
        )
        menu.menu_entry_index = terminal_menu.show()  / 2

        if menu.menu_entry_index == 0:
            import modules.osint_menu
            rerun()

        # if menu.menu_entry_index == 1:
        #     import modules.passes_menu
        #     rerun()

        # if menu.menu_entry_index == 2:
        #     import modules.decoder_menu
        #     rerun()

        if menu.menu_entry_index == 2:
            import modules.icao_tail_menu
            rerun()

        # if menu.menu_entry_index == 3:
        #     about()
        #     rerun()
        
        if menu.menu_entry_index == 4:
            console.print("[bold][blue] Exiting...[/blue][/bold]")
            sleep(1)

    menu()

except KeyboardInterrupt:
    print("\n")
    console.print("[bold][blue] Exiting...[/blue][/bold]")
    sleep(1)

except TypeError:
    os.system("clear")
    main_banner()
    console.print(f"\n[bold][red] INVALID COMMAND [/red][/bold]")
    rerun()