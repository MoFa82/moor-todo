# a cli todo app with ant theme
#TODO: consider making a menu class might be useful for future use
#TODO: Get the ascii art of an ant
#TODO: saving the info into json matters
#TODO: adding the ability to set timer
#TODO: Adding the colors styles needed to make the i/o more beautiful and emojies too
import json

class Group:
    def __init__(self, title):
        self.set_title(title)
        self.tasks = []
        self.group_dict = {}

    def set_title(self, title):
        self.title = title

    def del_task(self, index):
        del(self.tasks[index])
        return "Deleted the wanted task"

    def add_task(self, task):
        self.tasks.append(task)
        return "Task added succesfully"

    def get_title(self):
        return self.title

    def get_tasks(self):
        return self.tasks

    def print_group(self):
        print("======== " + self.get_title() + " ========")
        for i in self.get_tasks():
            print(str(i.get_marked()) + " " + i.get_desc())

    def to_dict(self):
        self.group_dict["title"] = self.get_title()
        self.group_dict["tasks"] = []
        task_dict = {}
        for i in self.get_tasks():
            task_dict[i.get_desc()] = i.get_marked()
            self.group_dict["tasks"].append(task_dict)
            task_dict.clear()
            self.group_dict.clear()

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
    with open("moor.json", "r") as f:
        pass
    f.close()

def save_to_disk(groups):
    with open("moor.json", "w") as json_file:
        for i in groups:
            json.dumps(i, json_file)
    json_file.close()

def update_file():
    with open("moor.json", "a") as f:
        pass
    f.close()

def new_group():
    pass

def print_all_groups(groups):
    print("========All groups=========")
    for i in range(len(groups)):
        print(i)
        groups[i].print_group()
        print("+++++++++++++\n")

def add_task_to_group(group):
    while True:
        print("Enter the task to add to the group\nIf you do not want enter cancel")
        inp = input()
        if inp == "cancel":
            print("OK CANCELED!")
            break
        else:
            task = Task(inp)
            print(group.add_task(task))
    return group


def main_menu():
    groups = []
    command = ""
    ANT_ART = """

              '=.
                           '=. \\
                              \\ \\
                           _,-=\\/=._        _.-,_
                          /         \\      /=-._ '-.
                         |=-./~\\___/~\\    /     `-._\
                         |   \\o/   \\o/   /         /
                          \\_   `~~~;/    |         |
                            `~,._,-'    /          /
                               | |      =-._      /
                           _,-=/ \\=-._     /|`-._/
                         //           \\   )\
                        /|             |)_.'/
                       //|             |\\_.''   _.-\\
                      (|  \\           /    _.`=    \\
                      ||   ":_    _.;"_.-;"   _.-=.:
                   _-."/    / `-."\\_."        =-_.;\
                  `-_./   /             _.-=.    / \\
                         |              =-_.;\\ .'   \\
                         \\                   \\/     \\
                         /\\_                .'\\      \\
                        //  `=_         _.-"   \\      \\
                       //      `~-.=`"`'       ||      ||
                       ||    _.-_/|            ||      |\\_.-_
                   _.-_/|   /_.-._/            |\\_.-_  \\_.-._\\
                  /_.-._/                      \\_.-._\\


    """
    while command != "0" or command != "exit":
        print(ANT_ART)
        print("hello, I'm Moori!\nI'm here to help you doing your tasks\nWhat can I do for you?\n")
        print("0- Exit\n1- Add new group\n2- Show all groups and tasks\n3- Toggle between groups")

        command = input()

        if command == "1":
            # new_group()
            print("Enter the title for the group:")
            title = input()
            group = Group(title)
            group = add_task_to_group(group)
            groups.append(group)

        elif command == "0" or command.lower() == "exit":
            save_to_disk(groups)
            print("Exiting")
            break

        elif command == "2":
            print_all_groups(groups)

        elif command == "3":
            print_all_groups(groups)
            print("Enter which group you want to toggle to:")
            inp = int(input())

            group = groups[inp]
            print("You chose %s\nWhat you want to do with it?", group.get_title())


if __name__ == "__main__" :
    main_menu()
