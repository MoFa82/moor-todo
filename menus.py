import functions
import colorize
import interface

def add_task_to_group_menu(group):
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

def new_group_menu():
    print(colorize.MAIN + "\nEnter the title for the group:")
    title = input()
    return functions.new_group(title)

def command_menu(ANT_ART, ANT_EMOJIE):
    print(colorize.MAIN + ANT_ART)
    print(colorize.MAIN + "hello, I'm Moori! " + ANT_EMOJIE + colorize.MAIN \
            + "\nI'm here to help you doing your tasks\nWhat can I do for you?\n")
    print(colorize.MAIN +
"""0- Exit
1- Add new group
2- Show all groups and tasks
3- Edit groups""")
    command = input()
    return command

def edit_task_menu(group):
    print(colorize.MAIN + "Enter the task you wanna change:")
    task_to_change = int(input())
    print(colorize.MAIN + "Enter the new decription:")
    desc = input()
    group = functions.edit_task(group, task_to_change, desc)
    if group != 0:
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

def delete_menu(groups, idx):
    # TODO: make sure that there is another confirm for delete
    try:
        del(groups[idx])
        print(colorize.SUC + "Deleted successfully\n")

    except IndexError:
        print(colorize.ERROR + "Out of range!\n")
    input()
    return groups

def mark_menu(group):
    print(colorize.MAIN + "\nEnter the task you want to mark:")
    the_task = int(input())
    try:
        group.get_tasks()[the_task].mark()
        print(colorize.SUC + "Task was marked")
    except IndexError:
        print(colorize.ERROR + "Out of range!\n")

    input()
    return group

def edit_menu(groups):
    functions.print_all_groups(groups)
    print(colorize.MAIN + "Enter which group you want to config:")

    try:
        inp = int(input())
    except ValueError:
        print(colorize.ERROR + "\nINVAlID\n")

    try:
        group = groups[inp]
    except IndexError:
        print(colorize.ERROR + "\nOut of range\n")
        input()

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
        group = edit_task_menu(group)

    elif sub_command == "2":
        group = add_task_menu(group)

    elif sub_command == "3":
        # TODO: make sure that there is another confirm for delete
        groups = delete_menu(groups, inp)

    elif sub_command == "4":
        group = mark_menu(group)

    return groups

def main_menu():
    groups = functions.init_groups()
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

        if command == "0" or command.lower() == "exit":
            print(colorize.MAIN + "Exiting")
            functions.save_to_disk(groups)
            break

        elif command == "1":
            groups.append(new_group_menu())

        elif command == "2":
            functions.print_all_groups(groups)

        elif command == "3":
            groups = edit_menu(groups)
