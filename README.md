# Student Task Manager

Project status: In Progress

A small console-based Python application for managing student tasks. It was
developed as a DevOps assignment with feature branches, merge conflict
resolution, automated tests, and GitHub Actions continuous integration.

## Features

- Add tasks with non-empty, case-insensitive duplicate validation.
- Display task IDs, titles, and pending/completed status.
- Complete tasks by numeric ID, including already-completed validation.
- Delete tasks by numeric ID with explicit confirmation.
- Exit through a simple interactive menu.

## Requirements

- Python 3.10 or newer (the application uses only the standard library).
- Git for the branch and history exercises.

## Installation and setup

Clone the repository and enter its directory:

```text
git clone https://github.com/taqishahje-creator/student-task-manager.git
cd student-task-manager
```

No third-party packages are required.

## Run the application

```text
py main.py
```

On systems where `python` is available, `python main.py` works as well.

## Example usage

```text
1. Add Task
Enter task title: Prepare presentation
Task added successfully!
2. Display Tasks
1. Prepare presentation - Pending
3. Complete Task
Enter Task ID to complete: 1
Task marked as completed!
```

Empty titles, duplicate titles, invalid IDs, and deletion without `yes` are
rejected with clear messages.

## Run automated tests

```text
py -m unittest discover -s tests -v
```

The same command is used by the GitHub Actions workflow in an environment
where `python` is available.

## GitHub Actions

`.github/workflows/python-tests.yml` runs the built-in unittest suite on every
push to `main` and every pull request targeting `main`. A failing test makes
the workflow fail.

## Project structure

```text
main.py                         Console application and task operations
tests/test_task_manager.py      Deterministic unittest suite
docs/userguide.md               User instructions and validation behavior
.github/workflows/python-tests.yml  Continuous integration workflow
LICENSE                         MIT License
```

## License

This project is released under the [MIT License](LICENSE).
