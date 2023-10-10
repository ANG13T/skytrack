from rich.console import Console

console = Console()

def generate_option(options):
    for i in range(options):
        print(i + 1 + ". " + options[i])

    res = console.print("[bold][blue] ENTER INPUT > [/blue][/bold]")

    if res < 1 or res > len(options):
        console.print("[bold red] INVALID OPTION [/bold red]")
        return None
    return res
