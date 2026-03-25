import csv
from datetime import datetime
import pandas as pd 

FILE_NAME = "expenses.csv" 

# Add Expense with Timestamp

def add_expense():
    item = input("Enter expense item: ")

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount.")
        return
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([item, amount, timestamp])

    print("✅ Expense recorded successfully.")


# Analyze Expenses using pandas

def analyze_expenses():
    try:
        df = pd.read_csv(FILE_NAME, names=["Item", "Amount", "Timestamp"])
        
        total = df["Amount"].sum()
        average = df["Amount"].mean()

        print("\n Expense Summary")
        print("---------------------")
        print(f"Total Spent: {total}")
        print(f"Average Expense: {average:.2f}")

    except FileNotFoundError:
        print("No expense file found.")

    except Exception as e:
        print(f"Error analyzing data: {e}")

    
# Main Menu

def main():
    while True:
        print("\n----- Expense Tracker -----")
        print("1. Add Expense")
        print("2. Analyze Expenses")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            analyze_expenses()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()