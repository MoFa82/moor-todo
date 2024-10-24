# a cli todo app with ant theme
#TODO: consider making a menu class might be useful for future use 
#TODO: Get the ascii art of an ant
#TODO: saving the info into json matters
#TODO: adding the ability to set timer
#TODO: Adding the colors styles needed to make the i/o more beautiful

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

    def print_tasks(self):
        for i in self.tasks:
            print(i.get_desc() + " " + str(i.get_marked()))

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

def task_menu(group):
    
    while True:

        print("Enter the task to add to the group\nIf you do not want enter cancel\n")
        inp = input()
        if inp == "cancel":
            print("OK CANCELED!\n")
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
        print("0 Exit\t1 Add new group\t2 Show all groups and tasks\n")

        command = input()

        if command == "1":
            # new_group()
            print("Enter the title for the group:\n")
            title = input()
            group = Group(title)
            group = task_menu(group)
            groups.append(group)

        if command == "0" or command.lower() == "exit":
            print("Exiting\n")
            break

        if command == "2":
            print("========All groups=========")
            for i in groups:
                i.print_tasks()
                print("\n")

if __name__ == "__main__" : 
    main_menu()
