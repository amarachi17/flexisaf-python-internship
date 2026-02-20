# Student Contact Manager (CLI)

Student Contact Manager is a Python console-based application designed to help school administrators manage student, parent, and staff contact information efficiently. 

This project demonstrates practical use of dictionaries, nested data structures, sets, validation logic, and CRUD operations.

---

## Features

- Add new contacts
- Update existing contact information
- Delete contacts
- Search contacts by unique ID
- List all stores contacts
- Prevent duplicate emails and phone numbers using sets
- Input validation for email and phone format

---

## Data Structure Design

- Contacts stored in a dictionary:
  ```python
  {
      unique_id: {
          "full_name": "...",
          "email": "...",
          "phone": "...",
          "role": "Student/Parent/Teacher"
      }
  }

- Sets used to enforce uniqueness:

used_emails
used_phones

## Technologies Used

- Python 3
- Dictionaries (nested)
- Sets
- CRUD operations
- Input validation
- Structured function design 

## How to Run
Navigate to the `week-06` directory and run:
python student_contact_manager.py

## Learning Objectives
- Master nested dictionaries
- Use sets for uniqueness control
- Implement full CRUD functionality
- Build structured, modular CLI apllications

## Author 
Confidence Amarachi Nkeonye