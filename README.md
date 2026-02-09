# To-Do List CLI (Python)

Minimal, file-backed to-do list CLI.

Install locally (editable) to get a `todo` command:

```bash
python -m pip install -e .
```

Then run:

```bash
todo add "Write report"
todo list
todo complete 0
todo remove 0
todo clear
```

Add with a due date:

```bash
todo add "Finish budget" --due 2026-02-15
todo add "Call client" --due tomorrow
```

If `todo` is not found, ensure your Python's `Scripts` directory is on your PATH (Windows) or use the same Python executable: `python -m todo`.

Run tests:

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```