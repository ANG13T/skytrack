from rich.console import Console

console = Console()

def main_banner():
    f = open('./assets/graphic.txt', 'r')
    content = f.read()
    console.print("[bold blue]" + content + "[/blue bold]")
    f = open('./assets/details.txt', 'r')
    details = f.read()
    console.print("[bold blue]" + details + "[/blue bold]")
    f.close()