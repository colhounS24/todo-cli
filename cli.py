#!/usr/bin/env python3
import argparse
import sys
from todo import ToDoList
from datetime import date, timedelta
from dateutil import parser as dateparser


def print_tasks(tasks):
    if not tasks:
        print("No tasks.")
        return
    today = date.today()
    for i, t in enumerate(tasks):
        status = "x" if t.get("done") else " "
        due = t.get("due")
        due_str = f" due: {due}" if due else ""
        overdue = ""
        if due and not t.get("done"):
            try:
                if date.fromisoformat(due) < today:
                    overdue = " [OVERDUE]"
            except Exception:
                pass
        print(f"[{status}] {i}: {t.get('title')}{due_str}{overdue}")


def main(argv=None):
    argv = argv or sys.argv[1:]
    parser = argparse.ArgumentParser(prog='todo', description='Simple To-Do CLI')
    parser.add_argument('--file', '-f', default='tasks.json', help='Path to tasks file')
    sub = parser.add_subparsers(dest='cmd')

    a_add = sub.add_parser('add', help='Add a task')
    a_add.add_argument('title', nargs='+', help='Task title')
    a_add.add_argument('--due', help='Due date (YYYY-MM-DD, today, tomorrow, or parseable date)')

    sub.add_parser('list', help='List tasks')

    a_complete = sub.add_parser('complete', help='Mark task complete')
    a_complete.add_argument('index', type=int, help='Task index')

    a_remove = sub.add_parser('remove', help='Remove task')
    a_remove.add_argument('index', type=int, help='Task index')

    sub.add_parser('clear', help='Remove all tasks')

    ns = parser.parse_args(argv)
    store = ToDoList(ns.file)

    if ns.cmd == 'add':
        title = ' '.join(ns.title)
        due_iso = None
        if getattr(ns, 'due', None):
            s = ns.due.strip().lower()
            if s == 'today':
                due_iso = date.today().isoformat()
            elif s == 'tomorrow':
                due_iso = (date.today() + timedelta(days=1)).isoformat()
            else:
                try:
                    dt = dateparser.parse(ns.due)
                    due_iso = dt.date().isoformat()
                except Exception:
                    print('Unable to parse due date:', ns.due)
                    return
        store.add(title, due_iso)
        print('Added:', title)
    elif ns.cmd == 'list' or ns.cmd is None:
        print_tasks(store.list())
    elif ns.cmd == 'complete':
        if store.complete(ns.index):
            print('Marked complete:', ns.index)
        else:
            print('Index out of range')
    elif ns.cmd == 'remove':
        if store.remove(ns.index):
            print('Removed:', ns.index)
        else:
            print('Index out of range')
    elif ns.cmd == 'clear':
        store.clear()
        print('All tasks removed')


if __name__ == '__main__':
    main()
