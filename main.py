# a cli todo app with ant theme
#TODO: consider making a menu class might be useful for future use 
#TODO: Get the ascii art of an ant
#TODO: saving the info into json matters
#TODO: adding the ability to set timer
#TODO: Adding the colors styles needed to make the i/o more beautiful and emojies too

class Group:
    def __init__(self, title):
        self.set_title(title)
        self.tasks = []

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

    def print_group(self):
        print("======== " + self.get_title() + " ========")    
        for i in self.tasks:
            print(str(i.get_marked()) + " " + i.get_desc())

class Task:
    def __init__(self, desc, marked=False):
        self.set_desc(desc)
        self.marked = marked
    
    def mark(self):
        self.marked != self.marked
           
    def set_desc(self, desc):
        self.desc = desc

    def get_desc(self):
        return self.desc

    def get_marked(self):
        return self.marked

def read_from_disk():
    pass

def save_to_disk():
    pass 

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
    while command != "0" or command != "exit":
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
