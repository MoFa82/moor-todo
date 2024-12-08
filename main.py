# a cli todo app with ant theme
import json
import colorama
colorama.init(autoreset=True)
from sys import platform
if platform == "win32" or platform == "cgwin" or platform == "msys":
    colorama.just_fix_windows_concole()
MAIN_COLOR = colorama.Style.DIM + colorama.Back.BLUE

class Group:
    def __init__(self, title, tasks=[]):
        self.set_title(title)
        self.tasks = []
        self.group_dict = {}

    def set_title(self, title):
        self.title = title

    def del_task(self, index):
        del(self.tasks[index])

    def add_task(self, task):
        self.tasks.append(task)

    def get_title(self):
        return self.title

    def get_tasks(self):
        return self.tasks

    def print_group(self):
        emoji = {"True":"\U00002705", "False":"\U0000274C"}
        print(colorama.Fore.CYAN +  "======== " + self.get_title() + " ========")
        for i in range(len(self.get_tasks())):
            print(colorama.Fore.BLUE + str(i) + " " + emoji[str(self.get_tasks()[i].get_marked())] + " " + self.get_tasks()[i].get_desc())

    def to_dict(self):
        self.group_dict["title"] = self.get_title()
        task_dict = {}
        self.group_dict["tasks"] = []
        for i in self.get_tasks():
            task_dict = {}
            task_dict["desc"] = i.get_desc()
            task_dict["marked"] = i.get_marked()
            self.group_dict["tasks"].append(task_dict)
        return self.group_dict

class Task:
    def __init__(self, desc, marked=False):
        self.set_desc(desc)
        self.marked = marked

    def mark(self):
        self.marked = not self.marked

    def set_desc(self, desc):
        self.desc = desc

    def get_desc(self):
        return self.desc

    def get_marked(self):
        return self.marked

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
    print(colorama.Fore.CYAN +  "========All groups=========")
    for i in range(len(groups)):
        print(i)
        groups[i].print_group()
        print(colorama.Fore.CYAN + "+++++++++++++\n")
        input()

def create_group_from_disk(dict_groups):
    groups = []
    for i in dict_groups:
        group = Group(i['title'])
        for j in i['tasks']:
            task = Task(j['desc'], j['marked'])
            group.add_task(task)
        groups.append(group)
    return groups

def add_task_to_group(group):
    while True:
        print(MAIN_COLOR +  "\nEnter the task to add to the group\nIf you do not want click enter")
        inp = input()
        if inp == "":
            print(colorama.Fore.LIGHTRED_EX + "OK CANCELED!\n")
            input()
            break
        else:
            task = Task(inp)
            group.add_task(task)
    return group

def new_group():
    print(MAIN_COLOR + "\nEnter the title for the group:")
    title = input()
    group = Group(title)
    group = add_task_to_group(group)
    return group

def command_menu(ANT_ART, ANT_EMOJIE):
    print(colorama.Fore.YELLOW + ANT_ART)
    print(MAIN_COLOR + "hello, I'm Moori! " + ANT_EMOJIE + MAIN_COLOR + "\nI'm here to help you doing your tasks\nWhat can I do for you?\n")
    print(MAIN_COLOR + "0- Exit\n1- Add new group\n2- Show all groups and tasks\n3- Edit groups")
    command = input()
    return command

def edit_task(group):
    print(MAIN_COLOR + "Enter the task you wanna change:")
    task_to_change = int(input())
    print(MAIN_COLOR + "Enter the new decription:")
    desc = input()
    try:
        group.get_tasks()[task_to_change].set_desc(desc)
    except IndexError:
        print(colorama.Fore.RED + "Out of range!\n")
        input()
        return
    print(colorama.Fore.GREEN + "Task is edited\n")
    input()
    return group

def add_task_menu(group):
    print(MAIN_COLOR + "\nEnter the task you want to add:")
    the_task = input()
    group.add_task(Task(the_task))
    print(colorama.Fore.GREEN + "Task added\n")
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
            print(MAIN_COLOR + "Exiting")
            save_to_disk(groups)
            break

        elif command == "2":
            print_all_groups(groups)

        elif command == "3":
            print_all_groups(groups)
            print(MAIN_COLOR + "Enter which group you want to config:")
            
            try:
                inp = int(input())
            except ValueError:
                print(colorama.Fore.RED + "\nINVAlID\n")
                continue 
            
            try:
                group = groups[inp]
            except IndexError:
                print(colorama.Fore.RED + "\nOut of range\n")
                input()
                continue

            print(MAIN_COLOR + "You chose " + group.get_title() + MAIN_COLOR + "\nWhat you want to do with it?")
            group.print_group()
            print(MAIN_COLOR + "\n0- Back\n1- Edit tasks\n2- Add tasks\n3- DELETE ENTIRE GROUP\n4- Check tasks as done")
            sub_command = input()

            if sub_command == "1":
                group = edit_task(group)

            elif sub_command == "2":
                group = add_task_menu(group)

            elif sub_command == "3":
                try:
                    del(groups[inp])
                except IndexError:
                    print(colorama.Fore.RED + "Out of range!\n")
                    input()
                    continue

                print(colorama.Fore.GREEN + "Deleted successfully\n")
                input()

            elif sub_command == "4":
                print(MAIN_COLOR + "\nEnter the task you want to mark:")
                the_task = int(input())
                try:
                    group.get_tasks()[the_task].mark()
                except IndexError:
                    print(colorama.Fore.RED + "Out of range!\n")
                    input()
                    continue
                print(colorama.Fore.GREEN + "Task was marked")
                input()

            else:
                continue

if __name__ == "__main__" :
    main()
