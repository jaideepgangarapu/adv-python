tasks = []
def show_tasks():
    if not tasks:
        print("No tasks available")
        return

    print("----- Tasks -----")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def add_task():
    task = input("Enter the task: ").strip()

    if task:
        tasks.append(task)
        print("Task added successfully")
    else:
        print("Task cannot be empty")


def remove_task():
    show_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter task number to remove: "))

        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            print(f"Removed: {removed}")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a number.")


def main():
    while True:
        print("\n===== TO-DO LIST =====")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_tasks()

        elif choice == "2":
            add_task()

        elif choice == "3":
            remove_task()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


main()