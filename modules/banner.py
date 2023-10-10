from rich.console import Console

console = Console()

def main_banner():
    f = open('./assets/graphic.txt', 'r', encoding="utf8")
    content = f.read()
    console.print("[bold blue]" + content + "[/blue bold]")
    f = open('./assets/details.txt', 'r', encoding="utf8")
    details = f.read()
    console.print("[bold blue]" + details + "[/blue bold]")
    f.close()