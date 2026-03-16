import argparse
from module.injector import injector_color

c1 = injector_color()

parse = argparse.ArgumentParser()
parse.add_argument("-u", "--url", help="Ссылка на сайт")
parse.add_argument("-t", "--threads", help="Ограничитель потоков")
args = parse.parse_args()

async def main():
    from module.dos_logic import dos_settings
    from module.interface import write_banner
    from rich.console import Console
    from module.clear import clear_screen
    pwaexho = Console()
    clear_screen()
    write_banner()

    if args.url and args.threads:
        await dos_settings(args.url, int(args.threads))
    else:
        pwaexho.print(f"\n\n{c1}> Пожалуйста, используйте так - python run.py -u <Ссылка> -t <Ограничитель>")
        exit(1)