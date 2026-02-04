"""
Secure Finance Assistant

Features:
1. Password strength checker
2. Expense tracker with summary

"""

# --------- PASSWORD STRENGTH CHECKER --------

def check_password_strength(password):
    score = 0
    tips = []

    if len(password) >= 8:
        score += 1
    else:
        tips.append("Use at least 8 characters. ")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        tips.append("Add at least one number. ")
    
    if any(char.isupper() for char in password):
        score += 1
    else:
        tips.append("Include an uppercase letter. ")

    if any(char.islower() for char in password):
        score += 1
    else:
        tips.append("Include a lowercase letter.")

    if any(char in "!@#$%^&*()_+-=" for char in password):
        score += 1
    else:
        tips.append("Add a special character (!@#$%...).")

    if score <= 2:
        strength = "Week"
    elif score == 3 or score == 4:
        strength = "Medium"
    else: 
        strength = "Strong"
    
    return strength, tips

# --------- EXPENSE TRACKER ---------

def expense_tracker():
    expenses = []

    while True:
        print("\n Type 'exit' to stop adding expenses.")
        amount_input = input("Enter expense amount: ")

        if amount_input.lower() == "exit":
            break

        amount = float(amount_input)
        category = input("Enter category (Food, Transport, etc): ")
        note = input("Enter note (optional): ")

        expense = {
            "amount": amount,
            "category": category,
            "note": note
        }

        expenses.append(expense)

        # Summary
        total_spent = 0
        category_totals = {}

        for expense in expenses:
            total_spent += expense["amount"]

            if expense["category"] in category_totals:
                category_totals[expense["category"]] += expense["amount"]
            else:
                category_totals[expense["category"]] = expense["amount"]

        print("\n ---- Expense Summary ----")
        print(f"Total Spent: ${total_spent}")

        for category, total in category_totals.items():
            print(f"{category}: ${total}")


# ---------------- MAIN PROGRAM -----------------

def main():
    print("Welcome on board ")

    password = input("Create a password to continue: ")
    strength, tips = check_password_strength(password)

    print(f"\n Password Strength: {strength}")

    if tips:
        print("Suggections to improve your password: ")
        for tip in tips:
            print(f"- {tip}")

    expense_tracker()
    print("\n Thank you for using this service")

if __name__ == "__main__":
    main()    