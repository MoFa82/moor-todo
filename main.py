# a cli todo app with ant theme

class Task:
    def __init__(self, desc, checked):
        self.desc = desc
        self.checked = checked

def read_from_memory():
    pass

def print_main_menu():
        print("hello, I'm Moori!\nI'm here to help you doing your tasks\nWhat can I do for you")

def main_menu():
    command = input()
    while command != 0 or command != "exit":
        pass
task = Task()
