
"""Console application and core operations for the Student Task Manager."""

tasks = []




def add_task(title=None):
    """Add a task, returning True when it is accepted."""
    if title is None:
        title = input("Enter task title: ").strip()
    else:
        title = str(title).strip()

    # Reject empty task titles
    if not title:
        print("Error: Task title cannot be empty!")
        return False

    # Prevent duplicate tasks
    for task in tasks:
        if task["title"].lower() == title.lower():
            print("Error: This task already exists!")
            return False

    # Create a new task
    task = {
        "id": max((item["id"] for item in tasks), default=0) + 1,
        "title": title,
        "completed": False
    }

    tasks.append(task)
    print("Task added successfully!")
    return True

def display_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\n--- Your Tasks ---")
    for task in tasks:
        status = "Completed" if task["completed"] else "Pending"
        print(f'{task["id"]}. {task["title"]} - {status}')


def _read_task_id(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("Error: Please enter a valid numeric Task ID!")
        return None


def complete_task(task_id=None):
    """Complete a task by ID, returning True when its state changes."""
    if task_id is None:
        display_tasks()
        if not tasks:
            return False
        task_id = _read_task_id("Enter Task ID to complete: ")
    else:
        try:
            task_id = int(task_id)
        except (TypeError, ValueError):
            print("Error: Please enter a valid numeric Task ID!")
            return False
    if task_id is None:
        return False
    for task in tasks:
        if task["id"] == task_id:
            if task["completed"]:
                print("This task is already completed!")
                return False
            task["completed"] = True
            print("Task marked as completed!")
            return True
    print("Error: Task ID not found!")
    return False


def delete_task(task_id=None, confirmation=None):
    """Delete a task by ID after confirmation, returning True on deletion."""
    if task_id is None:
        display_tasks()
        if not tasks:
            return False
        task_id = _read_task_id("Enter Task ID to delete: ")
    else:
        try:
            task_id = int(task_id)
        except (TypeError, ValueError):
            print("Error: Please enter a valid numeric Task ID!")
            return False
    if task_id is None:
        return False
    for task in tasks:
        if task["id"] == task_id:
            if confirmation is None:
                confirmation = input("Confirm deletion (yes/no): ").strip().lower()
            else:
                confirmation = str(confirmation).strip().lower()
            if confirmation != "yes":
                print("Deletion cancelled.")
                return False
            tasks.remove(task)
            print("Task deleted successfully!")
            return True
    print("Error: Task ID not found!")
    return False



def main():
    while True:
        print("\n===== Student Task Manager =====")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            display_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting Student Task Manager...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
