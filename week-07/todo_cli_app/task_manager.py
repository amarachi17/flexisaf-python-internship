# List to store tasks

tasks = []

def add_task():
    task = input("Enter new task: ").strip()

    if task == "":
        print("⚠ Task cannot be empty.")
        return
    
    tasks.append({"title": task, "completed": False})
    print("✅ Task added successfully.")


def view_tasks():
    if len(tasks) == 0:
        print("📭 No tasks available.")
        return
    
    print("\n📋 Your Tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "✔ Done" if task["completed"] else "❌ Not Done"
        print(f"{index}. {task['title']} - {status}")


def mark_task_done():
    if len(tasks) == 0:
        print("📭 No tasks to update.")
        return
    
    view_tasks()

    try: 
        task_number = int(input("Enter task number to mark as done: "))

        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
            print("✅ Task marked as done.")
        else:
            print("⚠ Invalid task number.")
    except ValueError:
        print("⚠ Please enter a valid number.")


def delete_task():
    if len(tasks) == 0:
        print("📭 No tasks to delete.")
        return
    
    view_tasks()

    try:
        task_number = int(input("Enter task number to delete: "))

        if 1 <= task_number <= len(tasks):
            removed = tasks.pop(task_number - 1)
            print(f"🗑 Task '{removed['title']}' deleted.")

        else:
            print("⚠ Invalid task number.")
    except ValueError:
        print("⚠ Please enter a valid number.")