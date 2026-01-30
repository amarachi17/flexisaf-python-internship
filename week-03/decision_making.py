# ----- AGE VALIDATOR ------

print("\n -------- Age Validator --------")
age = int(input("Enter your age: "))

if age >= 18:
    print("Status: Eligible")
else:
    print("Status: Not Eligible")

# ----- LOGIN FLOW ------

print("\n --------- Login Flow ---------- ")
correct_username = "admin"
correct_password = "password1234"

username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username and password == correct_password:
    print("Login successful")
else:
    print("Invalid username and password")

# ------ LOAN ELIGIBILITY CHECKER -------

print("\n ---------- Loan Eligibilty Checker ----------")
loan_age = int(input("Enter your age: "))
monthly_income = int(input("Enter your monthly income: "))
employment_status = input("Are you employed? (yes/no): ").lower()

if loan_age >=21 and monthly_income >= 100000 and employment_status == "yes":
    print("Loan Status: Approved")
else:
    print("Loan Status: Not Approved")

# ------- EXPENSE TRACKER -------

print("\n ---------- Expence Tracker ---------- ")
spending_limit = 50000
total_expenses = int(input("Enter your total expenses: "))

if total_expenses > spending_limit:
    print("Alert: Overspending detected")
else: 
    print("Spending is within the limit")