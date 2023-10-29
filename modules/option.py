from rich.console import Console

console = Console()


def generate_option(options):
    for i, item in enumerate(options):
        console.print("[cyan bold] [" + str(i + 1) + "] " +
                      item + "[/cyan bold] \n")

    res = console.input("[bold][blue] ENTER INPUT > [/blue][/bold]")

    if not res.isdigit() or int(res) < 1 or int(res) > len(options):
        console.print("[bold red] INVALID OPTION [/bold red]")
        return None

    console.print("\n")

    return int(res)
