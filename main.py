# a cli todo app with ant theme
import colorize
import interface
import functions
import menus
import json
import args
from colorama import init, just_fix_windows_console
from sys import platform, argv 

if platform == "win32" or platform == "cgwin" or platform == "msys":
    just_fix_windows_console()
init(autoreset=True)

if len(argv) > 1:
    args.arg_run(argv)

elif __name__ == "__main__":
    menus.main_menu()