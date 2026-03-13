# Learning Log - Flexisaf Internship

## Week 1
- Learned: Python basics, functions, file handling, JSON
- Built: User Profile Manager script
- Challenges: Input validation and file handling
- Improvements: Code structure and reusability

## Week 02
## Variables, Arithmetic and Logic

# What I Learned
- Using variables to store user input
- Performing arithemetic calculations
- Applying comparison and logical operators
- Implementing conditional statements for decision making

# Challenges Faced
- Understanding weighted scoring systems
- Differentiating between total and averge scores

# Key Takeaway
Real-world problems often require weighted logic rather than simple averages.


## Week 03
## Decision Making & Control Flow

# What I Learned
- How to use if and else statements to control program flow
- Applying comparison and logical operators to real-life problems
- Writing clear decision-making logic based on user input
- Structuring multiple tasks in a single Python script

# Tasks Completed
- Age validation program
- Login authentication flow
- Loan eligibility checker
- Expense tracker with overspending detection

# Challenges Faced
- Designing clear conditions for loan eligibility
- Ensuring login remains readable when handling multiple tasks in one file.

# Key Takeaway
Clear decision making logic is essential for building reliable applications, especially when handling user input and real world rules.

# Resources Used
- Programiz – Python if, elif, else  
  https://www.programiz.com/python-programming/if-elif
- Programming with Mosh – Python If Statements  
  https://youtu.be/6iF8Xb7Z3wQ


  ## Week 04
  ## Secure Finance Assistant

  # What I Learned
  This week focused on decision-making and loop-based logic in Python.
  I learned how to:

- Evaluate password strength using conditional checks
- Apply logical rules to score user input
- Use while loops for continuous user interaction
- Store structured data using lists and dictionaries
- Summarize data using for loops

# Challenges Faced
- Designing clear password evaluation rules
- Structuring expense data for easy summarization
- Ensuring the program remained user-friendly

# How I Solved Them
- Broke problems into smaller logical steps
- Used Python built-in functions like `any()`
- Added clear comments and meaningful variable names

# Outcome
I successfully built a console-based finance assistant that simulates real-world user interaction and demonstrates foundational backend skills.


## Week 05
## StudentHub CLI - Lists, Tuples $ List Comprehensions

# What I Learned
This week focused on mastering Python data structures, specifically lists and tuples.

I learned how to:
- Store structured data using lists
- Use tuples for fixed data storage
- Update and remove items from lists
- Use list comprehensions to filter data efficiently
- Structure larger programs using functions

# Practical Application

I built **StudentHub CLI**, a console application that:
- Manages academic assignments
- Tracks school-related expenses
- Filters expenses by category
- Identifies expenses above a certain amount

# Challenges Faced

- Managing nested data structures
- Designing clean menu navigation
- Understanding when to use tuples vs dictionaries

# Key Takeaway

List comprehensions are powerful and allow cleaner, more readable filtering logic compared to traditional loops.

# Resources Used

- Real Python – Lists and Tuples  
  https://realpython.com/python-lists-tuples/

- Python Lists & Tuples (YouTube)  
  https://youtu.be/R-HLU9Fl5ug


## Week 06
## Student Contact Manager (CLI)
## Dictionaries $ Sets

# Focus Area

This week focused on mastering Python dictionaried and sets.

# What I Learned

- How to use dictionaries to store structured records
- How nested dictionaries simulate database records
- How sets enforce uniqueness constraints
- Implementing full CRUD operations
- Validating user input before storing data

# Project Built

Student Contact Manager (CLI)

The program:
- Stores contacts using unique identifiers
- Prevents duplicate emails and phone numbers
- Supports adding, updating, deleting, searching, and listing contacts

# Challenges Faced

- Managing set updates during contact modification
- Handling validation before data insertion
- Designing clean function separation

# Key Takeaway

Sets are powerful tools for maintaining data interity, similar to UNIQUE constraints in databases. 

# Resources Used

- Real Python – Dictionaries  
  https://realpython.com/python-dicts/

- W3Schools – Python Dictionaries  
  https://www.w3schools.com/python/python_dictionaries.asp

- W3Schools – Python Sets  
  https://www.w3schools.com/python/python_sets.asp


## Week 07
## Functions & Modular Programming


# Focus Area

This week focused on creating reusable functions and structuring programs across multiple files.

# What I Learned

- How to define and call custom functions
- How to separate program logic into modules
- How to import functions from another file
- How to use built-in functions like len() and enumerate()
- How to handle invalid user input using try/except

# Project Built

CLI To-Do List App (Function-Based)

The application:
- Allows users to add, view, mark, and delete tasks
- Uses a dedicated file for task logic
- Separates menu logic into a main file
- Runs continuously until the user chooses to exit

# Challenges Faced

- Managing shared task data across files
- Ensuring user input does not crash the program
- Designing clean menu navigation

# Key Takeaway

Separating logic into multiple files improves readability, maintainability, and scalability. This approach reflects real-world software structure rathar tahn writing everything inside one script.

# Resources Used

- Programiz – Python Functions  
  https://www.programiz.com/python-programming/function

- Real Python – Defining Your Own Python Function  
  https://realpython.com/defining-your-own-python-function/


## Week 08
## Debugging & Error Handling


# Focus Area

This week focused on understanding how to sebug programs and handle errors when interacting with external systems such as APIs and files.

# What I Learned

- How to use `try/except` blocks to handle runtime errors
- How to work with external APIs using the `requests` library
- How to handle network errors, timeouts, and invalid responses
- How to safely read and write files using Python
- How to prevent accidental file overwrites

# Projects Completed

1. API Request Script
A script that retrieves data from a public API and handles connection errors, timeouts, and unexpected responses.

2. File Backup Tool
A script that copies the contents of a file into another file while preventing accidental overwrites and handling missing files.

# Challanges Faced

One challenge was anticipating the different types of errors that can occur when working with external services. I learned that defensive programming and proper exception handling make programs more reliable.

# Key Takeaway

Error handling is critical when building real-world software. Programs must anticipate and handle unexpected failures instead of crashing.

# Resources Used

- https://realpython.com/python-debugging/
- https://docs.python.org/3/tutorial/errors.html
- https://youtu.be/0ZvaDa8eT5s


## Week 09 
## CSV File Handling & Data Processing

# Focus Area

This week focused on working with CSV files to store and analyze structured data using Python.

# What I Learned

- How to create and write data to CSV files using the csv module
- How to read structured data from CSV files
- How to process stored data using loops
- How to calculate averages from datasets
- How to identify the highest value in a dataset

# Project Built

Student Score Manager

The program allows users to store student names and scores in a CSV file. The stored data is then analyzed to calculate the class average and determine the student with the highest score.

# Challenges Faced

One challenge was ensuring that the program correctly converts stored values into numeric data before performing calculations. Another challenge was handling cases where the CSV file does not exist.

# Key Takeaway

CSV files are a simple but powerful way to store structured data. Learning to read and analyze CSV data is useful for many real-world applications, including reporting and data analysis.

# Skills Strengthened

- File handling
- Data processing
- Python loops and aggregation
- Error handling
- Structured data management

# Resources Used

- https://realpython.com/read-write-files-python/
- https://realpython.com/python-csv/
- https://youtu.be/uhq5jZ6FaMY
- https://youtu.be/Da5TOXCwLSg

## Author 

Confidence Amarachi Nkeonye