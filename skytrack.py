import os
from rich.console import Console

console = Console()

try:
    from modules.menu import menu
except KeyboardInterrupt:
    os.system("clear")