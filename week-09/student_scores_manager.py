import csv

FILE_NAME = "student_scores.csv"


# Function to add student scores

def add_student_scores():
    print("\n Enter student records (type 'done' to stop).")
    
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)

        while True:
            name = input("Enter student name: ")

            if name.lower() == "done":
                break

            try:
                score = float(input("Enter student score: "))
                writer.writerow([name, score])
                print("Record saved successfully. \n")

            except ValueError:
                print("Invalid score. Please enter a number.")


# Function to analyze scores

def analyze_scores():
    students = []

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                name = row[0]
                score = float(row[1])
                students.append((name, score))

        if not students:
            print("No student records found. ")
            return
        
        total_score = sum(score for _, score in students)
        average_score = total_score / len(students)

        top_student = max(students, key=lambda x: x[1])

        print("\n Class Statistics")
        print("-------------------------------------")
        print(f"Total Students: {len(students)}")
        print(f"Class Avarage: {average_score: .2f}")
        print(f"Top Performer: {top_student[0]} ({top_student[1]})")

    except FileNotFoundError:
        print("Error: No CSV file found. Please add student scores first. ")

    except Exception as error:
        print(f"Unexpected error occurred: {error}")

# Main Program

def main():
    while True:
        print("\n ----- Student Score Manager -----")
        print("1. Add Student Scores")
        print("2. Analyze Scores")
        print("3. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            add_student_scores()

        elif choice == "2":
            analyze_scores()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose between 1-3.")


if __name__ == "__main__":
    main()    