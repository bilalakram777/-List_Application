## import json
import os

# File to store tasks
TASKS_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Display menu
def display_menu():
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

# Add a new task
def add_task(tasks):
    task_description = input("Enter task description: ")
    tasks.append({"description": task_description, "completed": False})
    print("Task added successfully!")

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    print("\nTasks:")
    for i, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Pending"
        print(f"{i}. {task['description']} [{status}]")

# Mark a task as completed
def mark_task_completed(tasks):
    if not tasks:
        print("No tasks to mark as completed.")
        return
    view_tasks(tasks)
    try:
        task_index = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks[task_index]["completed"] = True
            print(f"Task '{tasks[task_index]['description']}' marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Delete a task
def delete_task(tasks):
    if not tasks:
        print("No tasks to delete.")
        return
    view_tasks(tasks)
    try:
        task_index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            removed_task = tasks.pop(task_index)
            print(f"Task '{removed_task['description']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main function
def main():
    tasks = load_tasks()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Exiting. Tasks saved.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
