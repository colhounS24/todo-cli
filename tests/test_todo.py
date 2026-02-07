from todo import ToDoList


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
