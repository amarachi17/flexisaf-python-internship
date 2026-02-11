"""
StudentHub CLI 
A console-based school task and expense manager.

Features:
1. To-Do List Manager (add, view, complete, remove tasks)
2. Expense Tracker (store expenses as tuples)
3. Filter expenses using list comprehensions 

"""

# TO-DO LIST MANAGER

def todo_manager():
    tasks = []

    while True:
        print("\n ------ TO-DO LIST MENU ------")
        print("1. Add Assignment")
        print("2. View Assignments")
        print("3. Mark Assignment as Completed")
        print("4. Remove Assignment")
        print("5. Exist To-Do Manager")

        choice = input("Select an option: ")

        # Add Task
        if choice == "1":
            task = input("Enter assignment name: ")
            tasks.append({"task": task, "completed": False})
            print("Assignment added successfully.")

        # View Tasks
        elif choice == "2":
            if not tasks:
                print("No assignments yet.")
            else:
                for index, task in enumerate(tasks):
                    status = "✔ Completed" if task["completed"] else "❌ Pending"
                    print(f"{index + 1}. {task['task']} - {status}")

        # Mark as Completed
        elif choice == "3":
            task_number = int(input("Enter task number to mark complete: "))
            if 1 <= task_number <= len(tasks):
                tasks[task_number - 1]["completed"] = True
                print("Assignment marked as completed.")
            else: 
                print("Invalid task number.")

        # Remove Task
        elif choice == "4":
            task_number = int(input("Enter task number to remove: "))
            if 1 <= task_number <= len(tasks):
                removed = tasks.pop(task_number - 1)
                print(f"Removed: {removed['task']}")

            else: 
                print("Invalid task number.")
            
        # Exit 
        elif choice == "5":
            break

        else:
            print("Invalid option. Try again.")



# EXPENSE TRACKER

def expense_tracker():
    expenses = [] # List of tuples (category, amount)

    while True:
        print("\n ------ EXPENSE TRACKER MENU ------")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Filter by Category")
        print("4. Show Expenses Above Amount")
        print("5. Exit Expense Tracker")

        choice = input("Select an option: ")

        # Add Expense
        if choice == "1":
            category = input("Enter category (Lunch, Transport, Books): ")
            amount = float(input("Enter amount: "))
            expenses.append((category, amount))
            print("Expense added.")

        # View All Expenses
        elif choice == "2":
            if not expenses:
                print("No expenses recorded.")
            else: 
                for item in expenses:
                    print(f"{item[0]} - ${item[1]}")

        # Filter by Category (List Comprehension)
        elif choice == "3":
            search_category = input("Enter category to filter: ")
            filtered = [item for item in expenses if item[0].lower() == search_category.lower()]

            if filtered:
                for item in filtered:
                    print(f"{item[0]} - ${item[1]}")

            else:
                print("No matching expenses found.")

        # Expenses Above Certain Amount (List Comprehension)
        elif choice == "4":
            limit = float(input("Show expenses above amount: "))
            high_expenses = [item for item in expenses if item[1] > limit]

            if high_expenses:
                for item in high_expenses:
                    print(f"{item[0]} - ${item[1]}")

            else: 
                print("No expenses above that amount. ")

        # Exit 
        elif choice == "5":
            break

        else: 
            print("Invalid option. Try again. ")


# MAIN MENU

def main():
    while True:
        print("\n ------ StudentHub CLI -------")
        print("1. Manage Assignments")
        print("2. Manage Expenses")
        print("3. Exit Program")

        choice = input("Select an option: ")

        if choice == "1":
            todo_manager()
        elif choice == "2": 
            expense_tracker()
        elif choice == "3":
            print("Goodbye")
            break
        else:
            print("Invalid selection. ")
    
if __name__ == "__main__":
    main()