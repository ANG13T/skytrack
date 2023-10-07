from simple_term_menu import TerminalMenu
from time import sleep
# from modules.decoder import *
from rich.console import Console

console = Console()

def main_banner():
    f = open('./assets/graphic.txt', 'r')
    content = f.read()
    print("[bold blue]" + content + "[/blue bold]")
    f = open('./assets/details.txt', 'r')
    details = f.read()
    print("[bold blue]" + details + "[/blue bold]")
    f.close()

def main_menu():
    main_menu.options = [
        "🛰 Decode NOAA Recording",
        None,
        "📡 Resample NOAA Recording",
        None,
        "Exit Tool"
    ]
    main_menu.terminal_menu = TerminalMenu(
        main_menu.options,
        title="",
        menu_cursor=" ❯ ",
        menu_cursor_style=("fg_blue", "bold"),
        menu_highlight_style=("fg_cyan", "underline", "bold"),
    )
    main_menu.menu_entry_index = main_menu.terminal_menu.show() / 2

try:
    main_menu()
except KeyboardInterrupt:
    print("\n")
    console.print("[bold][cyan] Exiting skytrack [/cyan][/bold]")
    sleep(1)

except TypeError:
    # os.system("clear")
    console.print("\n[bold][red] INVALID COMMAND [/red][/bold]")
    # run_again()



main_banner()

