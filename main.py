# a cli todo app with ant theme
#TODO: consider making a menu class might be useful for future use
#TODO: adding the ability to set timer
#TODO: Adding the colors styles and emojies needed to make the i/o more beautiful
#TODO: splitting the code into functions and into multiple files
#TODO: Error handling for more robust coding
#TODO: create the visuality to enter, proceed cancel and checkbox

import json

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
        print("======== " + self.get_title() + " ========")
        for i in range(len(self.get_tasks())):
            print(str(i) + " " + emoji[str(self.get_tasks()[i].get_marked())] + " " + self.get_tasks()[i].get_desc())

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

def update_file():
    with open("moor.json", "w") as f:
        pass
    f.close()

def print_all_groups(groups):
    print("========All groups=========")
    for i in range(len(groups)):
        print(i)
        groups[i].print_group()
        print("+++++++++++++\n")
        input()

def new_group(dict_groups):
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
        print("\nEnter the task to add to the group\nIf you do not want click enter")
        inp = input()
        if inp == "":
            print("OK CANCELED!\n")
            input()
            break
        else:
            task = Task(inp)
            group.add_task(task)
    return group

def edit_group_menu():
    pass

def handle_index_error():
    pass

def main_menu():
    try:
        groups = new_group(read_from_disk())
    except KeyError:
        groups = []
    command = ""
    ANT_EMOJIE = "\U0001F41C"
    ANT_ART = r"""
                           '=. \
                              \ /
                           _,-=\/=._        _.-,_
                          /         \      /=-._ '-.
                         |=-./~\___/~\    /     `-.|_
                         |   \o/   \o/   /         /
                          \_   `~~~;/    |         |
                            `~,._,-'    /          /
                               | |      =-._      /
                           _,-=/ \=-._     /|`-._/
                         //           \   )\
                        /|             |)_.'/
                       //|             |\_.''   _.-\
                      (|  \           /    _.`=    \
                      ||   ":_    _.;"_.-;"   _.-=.:
                   _-."/    / `-."\_."        =-_.;\
                  `-_./   /             _.-=.    / \
                         |              =-_.;\\ .'   \
                         \                   \\/     \
                         /\_                .'\\      \
                        //  `=_         _.-"   \\      \
                       //      `~-.=`"`'       ||      ||
                       ||    _.-_/|            ||      |\_.-
                   _.-_/|   /_.-._/            |\_._  \_.-.-\
                  /_.-._/                      \_.-\

    """
    while command != "0" or command != "exit":
        print(ANT_ART)
        print("hello, I'm Moori! " + ANT_EMOJIE + "\nI'm here to help you doing your tasks\nWhat can I do for you?\n")
        print("0- Exit\n1- Add new group\n2- Show all groups and tasks\n3- Edit groups")
        command = input()

        if command == "1":
            # new_group()
            print("\nEnter the title for the group:")
            title = input()
            group = Group(title)
            group = add_task_to_group(group)
            groups.append(group)

        elif command == "0" or command.lower() == "exit":
            print("Exiting")
            save_to_disk(groups)
            break

        elif command == "2":
            print_all_groups(groups)

        elif command == "3":
            print_all_groups(groups)
            print("Enter which group you want to conifg:")
            inp = int(input())

            group = groups[inp]

            print("You chose " + group.get_title() + "\nWhat you want to do with it?")
            group.print_group()
            print("\n0- Back\n1- Edit tasks\n2- Add tasks\n3- DELETE ENTIRE GROUP\n4- Check tasks as done\n")
            sub_command = input()

            if sub_command == "1":
                print("Enter the task you wanna change:")
                task_to_change = int(input())
                print("Enter the new decription:")
                desc = input()
                group.get_tasks()[task_to_change].set_desc(desc)
                print("Task is edited\n")
                input()

            elif sub_command == "2":
                print("\nEnter the task you want to add:")
                the_task = input()
                group.add_task(Task(the_task))
                print("Task added\n")
                input()

            elif sub_command == "3":
                del(groups[inp])
                print("Deleted successfully\n")
                input()

            elif sub_command == "4":
                print("Enter the task you want to mark:")
                the_task = int(input())
                group.get_tasks()[the_task].mark()
                print("Task was marked")
                input()

            else:
                continue

if __name__ == "__main__" :
    main_menu()
