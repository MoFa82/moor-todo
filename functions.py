import colorize
import json
import interface
import menus 

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
        
def create_group_from_disk(dict_groups):
    groups = []
    for i in dict_groups:
        group = interface.Group(i['title'])
        for j in i['tasks']:
            task = interface.Task(j['desc'], j['marked'])
            group.add_task(task)
        groups.append(group)
    return groups

def new_group(title):
    group = interface.Group(title)
    group = menus.add_task_to_group_menu(group)
    return group

def edit_task(group, task_to_change, desc):
    try:
        group.get_tasks()[task_to_change].set_desc(desc)
    except IndexError:
        print(colorize.ERROR + "Out of range!\n")
        input()
        return 0

    return group

def init_groups():
    try:
        groups = create_group_from_disk(read_from_disk())
    except(KeyError, FileNotFoundError):
        groups = []
    return groups
