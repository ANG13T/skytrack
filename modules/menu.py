from modules import *
from time import sleep
from modules.rerun import rerun
# from modules.about import about
from rich.console import Console
from modules.banner import *
from modules.option import *
import os

console = Console()

try:
    main_banner()

    def menu():
        menu.options = [
            "🛫 Extract Information about Plane",
            "📘 Generate Flight Information PDF",
            "🛬 Tail Number and ICAO Conversion",
            "🧭 About and Usage",
            "Exit Tool",
        ]

        option = generate_option(menu.options)

        if option == None:
            rerun()
            return

        if option == 1:
            import modules.osint_menu
            rerun()

        # if menu.menu_entry_index == 1:
        #     import modules.passes_menu
        #     rerun()

        # if menu.menu_entry_index == 2:
        #     import modules.decoder_menu
        #     rerun()

        if option == 3:
            import modules.icao_tail_menu
            rerun()

        # if menu.menu_entry_index == 3:
        #     about()
        #     rerun()
        if option == 5:
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