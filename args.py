import functions
import colorize
import interface

def add_group(argv):
    group = interface.Group(argv[2])
    for i in argv[3:]:
        group.add_task(interface.Task(i))
    group.print_group()
    return group

def add_task(argv, group):
    try:
        group.add_task(interface.Task(argv[4]))
    except IndexError:
        print(colorize.ERROR + "Out of range!\n")
    return group

def mark_task(argv, group):
    try:
        group.mark_task(int(argv[4]))
        print(colorize.SUC + "Task was marked")
    except IndexError:
        print(colorize.ERROR + "Out of range!\n")
    return group

def edit_task(argv, group):
    try:
        group = functions.edit_task(group, int(argv[4]), argv[5])
    except IndexError:
        print(colorize.ERROR + "Out of range!\n")
    return group

def delete_group(argv, groups):
    try:
        del(groups[int(argv[2])])
        print(colorize.SUC + "Deleted successfully\n")
    except IndexError:
        print(colorize.ERROR + "Out of range!\n")
    return groups

def arg_run(argv):
    MAN = """
help: showing all the methods available

show_all or --ls : shows all the groups and tasks in order 

delete or --rm {n}: delete the group n

add_group --ag : create new group and add to previous

edit {n} --e {command}: editing the group number {n}

commands:
    add_task or --at {m}
    mark_task --mt {n}
    edit_task --et {n} {new_text}
"""
    groups = functions.create_group_from_disk(functions.read_from_disk())
    if argv[1] == "help" or argv[1] == "--h":
        print(colorize.HELP + MAN)

    elif argv[1] == "add_group" or argv[1] == "--ag":
        groups.append(add_group(argv))

    elif argv[1] == "show_all" or argv[1] == "--ls":
        functions.print_all_groups(groups)

    elif argv[1] == "edit" or argv[1] == "--e":
        group = groups[int(argv[2])]

        if argv[3] == "edit_task" or argv[3] == "--et":
            groups[int(argv[2])] = edit_task(argv, group)

        elif argv[3] == "add_task" or argv[3] == "--at": 
            groups[int(argv[2])] = add_task(argv, group)

        elif argv[3] == "mark_task" or argv[3] == "--mt":
            groups[int(argv[2])] = mark_task(argv, group)
           
        else:
            print(colorize.ERROR + "Unknown command")

    elif argv[1] == "delete" or argv[1] == "--rm":
        groups = delete_group(argv, groups)

    else:
        print(colorize.ERROR + "Unknown command")

    functions.save_to_disk(groups)
