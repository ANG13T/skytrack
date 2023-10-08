import os
from dotenv import load_dotenv
from rich.console import Console

console = Console()


try:
    def import_env():
        # load_dotenv()
        # N2YO_Key = os.getenv('N2YO_API')
        # if N2YO_Key == "API_KEY_HERE":
        #     console.print("[bold blue]Put N2YO API Key in .env file[/]")
        #     return False
        # else:
        #     return True
        return True

    if import_env():
        from modules.menu import menu

except KeyboardInterrupt:
    os.system("clear")
    console.print("\n")
    console.print("[bold][blue] Exiting...[/blue][/bold]")