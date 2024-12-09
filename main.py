# a cli todo app with ant theme
import colorize
import interface
import functions
from colorama import init, just_fix_windows_console
from sys import platform

if platform == "win32" or platform == "cgwin" or platform == "msys":
    just_fix_windows_console()
init(autoreset=True)

def main():
    try:
        groups = functions.create_group_from_disk(functions.read_from_disk())
    except (KeyError, FileNotFoundError):
        groups = []
    command = ""
    ANT_EMOJIE = "\U0001F41C"
    ANT_ART = r"""
                              _            _
 _ __ ___   ___   ___  _ __  | |_ ___   __| | ___
| '_ ` _ \ / _ \ / _ \| '__| | __/ _ \ / _` |/ _ \
| | | | | | (_) | (_) | |    | || (_) | (_| | (_) |
|_| |_| |_|\___/ \___/|_|     \__\___/ \__,_|\___/
    """

    while command != "0" or command != "exit":
        command = functions.command_menu(ANT_ART, ANT_EMOJIE)

        if command == "1":
            groups.append(functions.new_group())

        elif command == "0" or command.lower() == "exit":
            print(colorize.MAIN + "Exiting")
            functions.save_to_disk(groups)
            break

        elif command == "2":
            functions.print_all_groups(groups)

        elif command == "3":
            functions.print_all_groups(groups)
            print(colorize.MAIN + "Enter which group you want to config:")

            try:
                inp = int(input())
            except ValueError:
                print(colorize.ERROR + "\nINVAlID\n")
                continue

            try:
                group = groups[inp]
            except IndexError:
                print(colorize.ERROR + "\nOut of range\n")
                input()
                continue

            print(colorize.MAIN + "You chose " + group.get_title() \
                    + colorize.MAIN + "\nWhat you want to do with it?")
            group.print_group()
            print(colorize.MAIN + """
0- Back
1- Edit tasks
2- Add tasks
3- DELETE ENTIRE GROUP
4- Check tasks as done""")
            sub_command = input()

            if sub_command == "1":
                group = functions.edit_task(group)

            elif sub_command == "2":
                group = functions.add_task_menu(group)

            elif sub_command == "3":
                try:
                    del(groups[inp])
                except IndexError:
                    print(colorize.ERROR + "Out of range!\n")
                    input()
                    continue

                print(colorize.SUC + "Deleted successfully\n")
                input()

            elif sub_command == "4":
                print(colorize.MAIN + "\nEnter the task you want to mark:")
                the_task = int(input())
                try:
                    group.get_tasks()[the_task].mark()
                except IndexError:
                    print(colorize.ERROR + "Out of range!\n")
                    input()
                    continue
                print(colorize.SUC + "Task was marked")
                input()

            else:
                continue

if __name__ == "__main__" :
    main()
