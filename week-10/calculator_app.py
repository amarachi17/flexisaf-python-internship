import math_tools

def main():
    print("----- Simple Calculator -----")

    while True:
        print("\n Choose an operation: ")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == "5":
            print("Goodbye!")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                result = math_tools.add(num1, num2)

            elif choice == "2":
                result = math_tools.subtract(num1, num2)
            
            elif choice == "3":
                result = math_tools.multiply(num1, num2)

            elif choice == "4":
                result = math_tools.divide(num1, num2)

            print(f"Result: {result}")

        except ValueError:
            print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    main()