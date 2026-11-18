# Student Task Manager User Guide

The application is a console menu for managing student tasks.

## Start the application

From the project directory, run:

```text
py main.py
```

Choose `5` to exit.

## Add a task

Choose `1`, then enter a non-empty title. Titles are trimmed and compared
case-insensitively, so a duplicate title is rejected.

## View tasks

Choose `2`. Each task shows its numeric ID, title, and `Pending` or `Completed`
status. If there are no tasks, the application reports that none are available.

## Complete a task

Choose `3` and enter an existing numeric task ID. An unknown or non-numeric ID
produces a validation error. Completing an already completed task is rejected.

## Delete a task

Choose `4` and enter an existing numeric task ID. Confirm with `yes` to delete;
any other response cancels the deletion. Unknown and non-numeric IDs produce a
validation error.
