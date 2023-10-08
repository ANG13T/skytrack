def main_banner():
    f = open('./assets/graphic.txt', 'r')
    content = f.read()
    print("[bold blue]" + content + "[/blue bold]")
    f = open('./assets/details.txt', 'r')
    details = f.read()
    print("[bold blue]" + details + "[/blue bold]")
    f.close()