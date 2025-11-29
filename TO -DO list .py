# To-Do List Manager

tasks = []  
completed_tasks_set = set() 

filename = "todo_list.txt"

def load_tasks():
    try:
        with open(filename, "r") as file:
            for line in file:
                
                task_name, status = line.strip().split(",")
                tasks.append({"task": task_name, "status": status})
                if status == "done":
                    completed_tasks_set.add(task_name.lower())
    except FileNotFoundError:
        pass

def save_tasks():
    with open(filename, "w") as file:
        for task in tasks:
            file.write(f"{task['task']},{task['status']}\n")


def format_task_name(name):
    return " ".join(word.capitalize() for word in name.split())

def add_task():
    name = input("Enter task description: ").strip()
    formatted_name = format_task_name(name)
    status = "pending"
    
    if "urgent" in formatted_name.lower():
        tasks.insert(0, {"task": formatted_name, "status": status})
    else:
        tasks.append({"task": formatted_name, "status": status})
    print(f"Task '{formatted_name}' added.")
    
def view_tasks():
    if not tasks:
        print("No tasks to display.")
        return
    print("Tasks List:")
    for i, task in enumerate(tasks, 1):
        status = "✓" if task['status'] == "done" else "✗"
        print(f"{i}. {task['task']} [{status}]")

def complete_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to complete: "))
        if 1 <= task_num <= len(tasks):
            task = tasks[task_num - 1]
            if task['status'] == "done":
                print(f"Task '{task['task']}' is already completed.")
            else:
                task['status'] = "done"
                completed_tasks_set.add(task['task'].lower())
                print(f"Task '{task['task']}' marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    load_tasks()
    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Save and Exit")
        print("5. Exit without Saving")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            save_tasks()
            print("Tasks saved. Goodbye!")
            break
        elif choice == "5":
            confirm = input("Exit without saving? (yes/no): ").strip().lower()
            if confirm == "yes":
                print("Goodbye without saving!")
                break
        else:
            print("Invalid choice! Please select from 1 to 5.")

if __name__ == "__main__":
    main()
