# a cli todo app with ant theme
import json
import colorize
import interface
from colorama import init, just_fix_windows_console
from sys import platform

if platform == "win32" or platform == "cgwin" or platform == "msys":
    just_fix_windows_console()
init(autoreset=True)

def read_from_disk():
    dict_groups = []
    with open("moor.json", "r") as f:
        for group in f:
            dict_groups.append(json.loads(group))
    f.close()
    return dict_groups

def save_to_disk(groups):
    with open("moor.json", "w") as json_file:
        for i in groups:
            json_group = json.dumps(i.to_dict())
            json_file.write(json_group)
            json_file.write("\n")
    json_file.close()

def print_all_groups(groups):
    print(colorize.SEP +  "========All groups=========")
    for i in range(len(groups)):
        print(i)
        groups[i].print_group()
        print(colorize.SEP + "+++++++++++++\n")
        input()

def create_group_from_disk(dict_groups):
    groups = []
    for i in dict_groups:
        group = interface.Group(i['title'])
        for j in i['tasks']:
            task = interface.Task(j['desc'], j['marked'])
            group.add_task(task)
        groups.append(group)
    return groups

def add_task_to_group(group):
    while True:
        print(colorize.MAIN + \
                "\nEnter the task to add to the group\nIf you do not want click enter")
        inp = input()
        if inp == "":
            print(colorize.ERROR + "OK CANCELED!\n")
            input()
            break
        else:
            task = interface.Task(inp)
            group.add_task(task)
    return group

def new_group():
    print(colorize.MAIN + "\nEnter the title for the group:")
    title = input()
    group = interface.Group(title)
    group = add_task_to_group(group)
    return group

def command_menu(ANT_ART, ANT_EMOJIE):
    print(colorize.OBJECT + ANT_ART)
    print(colorize.MAIN + "hello, I'm Moori! " + ANT_EMOJIE + colorize.MAIN \
            + "\nI'm here to help you doing your tasks\nWhat can I do for you?\n")
    print(colorize.MAIN + "0- Exit\n1- Add new group\n2- Show all groups and tasks\n3- Edit groups")
    command = input()
    return command

def edit_task(group):
    print(colorize.MAIN + "Enter the task you wanna change:")
    task_to_change = int(input())
    print(colorize.MAIN + "Enter the new decription:")
    desc = input()
    try:
        group.get_tasks()[task_to_change].set_desc(desc)
    except IndexError:
        print(colorize.ERROR + "Out of range!\n")
        input()
        return
    print(colorize.SUC + "Task is edited\n")
    input()
    return group

def add_task_menu(group):
    print(colorize.MAIN + "\nEnter the task you want to add:")
    the_task = input()
    group.add_task(interface.Task(the_task))
    print(colorize.SUC + "Task added\n")
    input()
    return group

def main():
    try:
        groups = create_group_from_disk(read_from_disk())
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
        command = command_menu(ANT_ART, ANT_EMOJIE)

        if command == "1":
            groups.append(new_group())

        elif command == "0" or command.lower() == "exit":
            print(colorize.MAIN + "Exiting")
            save_to_disk(groups)
            break

        elif command == "2":
            print_all_groups(groups)

        elif command == "3":
            print_all_groups(groups)
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
            print(colorize.MAIN + "\n0- Back\n1- Edit tasks\n2- Add tasks\n3- DELETE ENTIRE GROUP\n4- Check tasks as done")
            sub_command = input()

            if sub_command == "1":
                group = edit_task(group)

            elif sub_command == "2":
                group = add_task_menu(group)

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
