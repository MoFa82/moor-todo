import colorize
import json
import interface

def read_from_disk():
    dict_groups = []
    with open("moor.json", "r") as f:
        for group in f:
            dict_groups.append(json.loads(group))
    f.close()
    return dict_groups

# TODO: make save to disk into 2 function one for group and other for list
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

def new_group(title):
    group = interface.Group(title)
    group = add_task_to_group(group)
    return group

def command_menu(ANT_ART, ANT_EMOJIE):
    print(colorize.OBJECT + ANT_ART)
    print(colorize.MAIN + "hello, I'm Moori! " + ANT_EMOJIE + colorize.MAIN \
            + "\nI'm here to help you doing your tasks\nWhat can I do for you?\n")
    print(colorize.MAIN +
"""0- Exit
1- Add new group
2- Show all groups and tasks
3- Edit groups""")
    command = input()
    return command
#BUG: does not change the task
def edit_task(group, task_to_change, desc):
    try:
        group.get_tasks()[task_to_change].set_desc(desc)
    except IndexError:
        print(colorize.ERROR + "Out of range!\n")
        input()
        return 0

    return group

def edit_task_menu(group):

    print(colorize.MAIN + "Enter the task you wanna change:")
    task_to_change = int(input())
    print(colorize.MAIN + "Enter the new decription:")
    desc = input()
    group = edit_task(group, task_to_change, desc)
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
