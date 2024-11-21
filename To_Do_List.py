# Simple To-Do List Application

def display_menu():
    print("\nSimple To-Do List")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def view_tasks(tasks):
    if tasks:
        print("\nYour To-Do List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    else:
        print("\nYour To-Do List is empty!")

def add_task(tasks):
    task = input("\nEnter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added!")

def remove_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_number = int(input("\nEnter the task number to remove: "))
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f"Task '{removed_task}' removed!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("\nChoose an option (1-4): ")
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again!")

if __name__ == "__main__":
    main()
