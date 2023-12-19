from rich.console import Console

console = Console()

def main_banner():
    f = open('./assets/graphic.txt', 'r', encoding="utf8")
    content = f.read()
    console.print(f"[bold blue]{content}[/blue bold]")
    with open('./assets/details.txt', 'r', encoding="utf8") as f:
        details = f.read()
        console.print(f"[bold blue]{details}[/blue bold]")