# a cli todo app with ant theme
# next step: make it work with arguments
import colorize
import interface
import functions
import json
from colorama import init, just_fix_windows_console
from sys import platform, argv 

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
            print(colorize.MAIN + "\nEnter the title for the group:")
            title = input()
            groups.append(functions.new_group(title))

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
                group = functions.edit_task_menu(group)

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

def arg_run(args=argv):

    groups = functions.create_group_from_disk(functions.read_from_disk())
    if argv[1] == "help" or argv[1] == "--h":
        print("""
            help: showing all the methods available
            show_all: shows all the groups and tasks in order 
            add_group: create new group and add to previous
            edit {n} {command}: editing the group number {n}
                add_task:
                delete:
                check_task:
                edit_task: {m} {new_text}
            """)

    elif argv[1] == "add_group":
        tasks = []
        group = interface.Group(argv[2])
        for i in argv[3:]:
            group.add_task(interface.Task(i))
        group.print_group()

        with open("moor.json", "a") as json_file:
            json_group = json.dumps(group.to_dict())
            json_file.write(json_group)
            json_file.write("\n")
        json_file.close()

    elif argv[1] == "show_all":
        functions.print_all_groups(groups)

    elif argv[1] == "edit":
        if argv[3] == "edit_task":
            groups[int(argv[2])] = functions.edit_task(groups[int(argv[2])], int(argv[4]), argv[5])
            
        elif argv[3] == "add_task": 
            group = groups[int(argv[2])]
            group.add_task(interface.Task(argv[4]))

        elif argv[3] == "check_task":
            group = groups[int(argv[2])]
            group.get_tasks()[int(argv[4])].mark()


        else:
            print(colorize.ERROR + "Unknown command")

    elif argv[1] == "delete":
        del(groups[int(argv[2])])

    else:
        print(colorize.ERROR + "Unknown command")

    functions.save_to_disk(groups)


if len(argv) > 1:
    arg_run()

elif __name__ == "__main__":
    main()
