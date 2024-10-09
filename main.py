# a cli todo app with ant theme

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
    
    def mark(self)
        self.marked = !self.marked
           
    def set_desc(self, desc):
        self.desc = desc

def read_from_memory():
    pass

def print_main_menu():
        print("hello, I'm Moori!\nI'm here to help you doing your tasks\nWhat can I do for you")

def main_menu():
    command = input()
    while command != 0 or command != "exit":
        pass
