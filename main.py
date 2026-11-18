
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


def complete_task():
    display_tasks()

    if not tasks:
        return

    try:
        task_id = int(input("Enter Task ID to complete: "))

        for task in tasks:
            if task["id"] == task_id:
                task["completed"] = True
                print("Task marked as completed!")
                return

        print("Error: Task ID not found!")

    except ValueError:
        print("Error: Please enter a valid numeric Task ID!")




def main():
    while True:
        print("\n===== Student Task Manager =====")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Complete Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            display_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            print("Exiting Student Task Manager...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
