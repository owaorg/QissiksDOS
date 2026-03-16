from rich.console import Console
pwaexho = Console()

from module.injector import injector_color
from rich.align import Align
color = injector_color()

def write_banner():
    banner = rf'''{color}   ____  _         _ _        
  / __ \(_)       (_) |       
 | |  | |_ ___ ___ _| | _____ 
 | |  | | / __/ __| | |/ / __|
 | |__| | \__ \__ \ |   <\__ \
  \___\_\_|___/___/_|_|\_\___/'''
    pwaexho.print(Align.center(banner))
    