from todos import  TaskManager, Action, Action2


def test_can_create_an_action():
    action = Action("add", "first task", 1)
    assert action.name == "add"
    assert action.description == "first task"
    assert action.numero == 1

def test_can_delete_an_action():
    action = Action2()



def test_can_create_a_task_manager():
    task_manager = TaskManager()


def test_task_manager_starts_with_no_tasks():
    task_manager = TaskManager()

    assert task_manager.tasks == []


def test_parse_add():
    command = "+ first task"
    task_manager = TaskManager()
    numero = 1

    action = task_manager.parseadd(command, numero)

    assert action.name == "add"
    assert action.description == "first task"
    assert action.numero == 1

def test_parse_del():
    command = "- first task"
    numero = 1
    task_manager = TaskManager()

    action = task_manager.parsedel(command,numero)
    assert action.name == "del"
    assert action.numero == 1