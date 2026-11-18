
# Student Task Manager
# Initial version: Add and Display Tasks

tasks = []


def add_task():
    title = input("Enter task title: ")
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!")


def display_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\n--- Your Tasks ---")
    for task in tasks:
        status = "Completed" if task["completed"] else "Pending"
        print(f'{task["id"]}. {task["title"]} - {status}')


def main():
    while True:
        print("\n===== Student Task Manager =====")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            display_tasks()
        elif choice == "3":
            print("Exiting Student Task Manager...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
