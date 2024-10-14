# a cli todo app with ant theme
#TODO: consider making a menu class might be useful for future use 
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

class Task:
    def __init__(self, desc, marked):
        set_desc(desc)
        self.marked = marked
    
    def mark(self):
        self.marked != self.marked
           
    def set_desc(self, desc):
        self.desc = desc

def read_from_disk():
    pass

def main_menu():
    command = ""
    while command != "0" or command != "exit":
        print("hello, I'm Moori!\nI'm here to help you doing your tasks\nWhat can I do for you")
        print("0 Exit\t1 Add new group\t")

        command = input()

        if command == "1":
            # new_group()
            print("Enter the title for the group:")
            title = input()
            group = Group(title)
            
            
main_menu()
