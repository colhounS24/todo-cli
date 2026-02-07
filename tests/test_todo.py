from datetime import date

try:
    from todo import ToDoList
except Exception:
    from todo_cli.todo import ToDoList


def test_add_and_list_and_complete_and_remove(tmp_path):
    p = tmp_path / "tasks.json"
    store = ToDoList(str(p))

    store.add('task one')
    store.add('task two')
    tasks = store.list()
    assert len(tasks) == 2
    assert tasks[0]['title'] == 'task one'

    assert store.complete(0) is True
    tasks = store.list()
    assert tasks[0]['done'] is True

    assert store.remove(1) is True
    tasks = store.list()
    assert len(tasks) == 1

    store.clear()
    assert store.list() == []


def test_due_date_is_stored(tmp_path):
    p = tmp_path / "tasks.json"
    store = ToDoList(str(p))

    store.add('due task', due='2026-02-08')
    tasks = store.list()
    assert len(tasks) == 1
    assert tasks[0]['due'] == '2026-02-08'


def test_due_today_filter(tmp_path):
    p = tmp_path / "tasks.json"
    store = ToDoList(str(p))

    today = date.today().isoformat()
    store.add('today task', due=today)
    store.add('future task', due='2099-01-01')

    res = store.due_today()
    assert len(res) == 1
    assert res[0]['title'] == 'today task'
