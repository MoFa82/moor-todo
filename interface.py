from colorize import SEP, TASK
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
        print(SEP +  "======== " + self.get_title() + " ========")
        for i in range(len(self.get_tasks())):
            print(TASK + str(i) + " " \
                    + emoji[str(self.get_tasks()[i].get_marked())] + " " + self.get_tasks()[i].get_desc())

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
    
    def mark_task(self, index):
        self.tasks[index].mark()

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
