"""
Student Contact Manager (CLI)

A console-based contact management system for schools.
Uses: 
- Dictionary for storing contacts
- Nested dictionaries for contact details
- Sets to prevent duplicate emails and phone numbers

"""

# DATA STORAGE

contacts = {} # Main dictionary: {unique_id: {contact_details} }
used_emails = set()
used_phones = set()


# VALIDATION FUNCTIONS

def is_valid_email(email):
    return "@" in email and "." in email

def is_valid_phone(phone):
    return phone.isdigit() and len(phone) >= 7


# ADD CONTACT

def add_contact():
    unique_id = input("Enter unique ID (Student ID or Email): ") 

    if unique_id in contacts:
        print("❌ A contact with this ID already exists.")
        return
    
    full_name = input("Enter full name: ")
    email = input("Enter email: ")
    phone = input("Enter phone number: ")
    role = input("Enter role (Student/Parent/Teacher): ")

    # Validation 
    if not is_valid_email(email):
        print("❌ Invalid email format. ")
        return
    
    if not is_valid_phone(phone):
        print("❌ Invalid phone number.")
        return
    
    if email in used_emails:
        print("❌ This email is already in use.")
        return
    
    if phone in used_phones:
        print("❌ This phone number is already in use.")
        return
    
    # Store Contact
    contacts[unique_id] = {
        "full_name": full_name,
        "email": email,
        "phone": phone,
        "role": role 
    }

    used_emails.add(email)
    used_phones.add(phone)

    print("✅ Contact added successfully.")


# UPDATE CONTACT

def update_contact():
    unique_id = input("Enter the unique ID of the contact to update: ")

    if unique_id not in contacts:
        print("❌ Contact not found.")
        return
    
    contact = contacts[unique_id]

    print("Leave field blank to keep current value.")

    new_name = input(f"Full Name ({contact['full_name']}): ")
    new_email = input(f"Email ({contact['email']}): ")
    new_phone = input(f"Phone ({contact['phone']}): ")
    new_role = input(f"role ({contact['role']}): ")

    # Update name 
    if new_name:
        contact["full_name"] = new_name
    
    # Update email
    if new_email:
        if not is_valid_email(new_email):
            print("❌ Invalid email format. ")
            return
        if new_email in used_emails:
            print("❌ Email already in use. ")
            return
        
        used_emails.remove(contact["email"])
        used_emails.add(new_email)
        contact["email"] = new_email

    # Update phone
    if new_phone:
        if not is_valid_phone(new_phone):
            print("❌ Invalid phone number.")
            return
        if new_phone in used_phones:
            print("❌ Phone number already in use.")
            return
        
        used_phones.remove(contact["phone"])
        used_phones.add(new_phone)
        contact["phone"] = new_phone

    # Update role 
    if new_role:
        contact["role"] = new_role

    print("✅ Contact updated successfully.")


# DELETE CONTACT

def delete_contact():
    unique_id = input("Enter unique ID of contact to delete: ")

    if unique_id not in contacts:
        print("❌ Contact not found. ")
        return
    
    contact = contacts.pop(unique_id)

    used_emails.remove(contact["email"])
    used_phones.remove(contact["phone"])

    print("✅ Contact deleted successfully.")


# SEARCH CONTACT

def search_contact():
    unique_id = input("Enter unique ID to search: ")

    if unique_id in contacts:
        contact = contacts[unique_id]
        print("\n ----- Contact Found -----")
        for key, value in contact.items():
            print(f"{key}: {value}")
    
    else:
        print("❌ Contact not found.")


# LIST ALL CONTACTS

def list_contacts():
    if not contacts:
        print("No contacts available.")
        return
    
    print("\n ----- All Contacts -----")
    for unique_id, details in contacts.items():
        print(f"\n ID: {unique_id}")
        for key, value in details.items():
            print(f"{key}: {value}")


# MAIN MENU

def main():
    while True: 
        print("\n ---------- Student Contact Manager ----------")
        print("1. Add Contact")
        print("2. Update Contact")
        print("3. Delete Contact")
        print("4. Search Contact")
        print("5. List All Contacts")
        print("6. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            update_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            search_contact()
        elif choice == "5": 
            list_contacts()
        elif choice == "6":
            print("Goodbye 👋")
            break
        else:
            print("Invalid selection.")
        

if __name__ == "__main__":
    main()