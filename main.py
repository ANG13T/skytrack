from rich import print

def main_banner():
    f = open('./assets/graphic.txt', 'r')
    content = f.read()
    print("[bold][blue]" + content + "[/blue][/bold]")
    f.close()


main_banner()