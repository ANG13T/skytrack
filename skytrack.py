import os
from rich.console import Console

console = Console()


try:
    from modules.menu import menu
except KeyboardInterrupt:
    os.system("clear")
    console.print("n")
    console.print("[bold][blue] Exiting...[/blue][/bold]")