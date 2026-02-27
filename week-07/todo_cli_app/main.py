from task_manager import add_task, view_tasks, mark_task_done, delete_task

def show_menu():
    print("\n ------- CLI To-Do List App -------")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1 - 5): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_task_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("⚠ Invalid choice. Please select a number between 1 and 5.")

if __name__ == "__main__":
    main()        