#!/usr/bin/env python3
import argparse
import sys
from todo import ToDoList

def print_tasks(tasks):
    if not tasks:
        print("No tasks.")
        return
    for i, t in enumerate(tasks):
        status = "x" if t.get("done") else " "
        print(f"[{status}] {i}: {t.get('title')}")

def main(argv=None):
    argv = argv or sys.argv[1:]
    parser = argparse.ArgumentParser(prog='todo', description='Simple To-Do CLI')
    parser.add_argument('--file', '-f', default='tasks.json', help='Path to tasks file')
    sub = parser.add_subparsers(dest='cmd')

    a_add = sub.add_parser('add', help='Add a task')
    a_add.add_argument('title', nargs='+', help='Task title')

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
        store.add(title)
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
