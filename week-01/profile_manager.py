import json
import os

def collect_profile():
    # Collet user profile information interactively and validate inputs.
    print("Please enter your profile details: ")
    
    while True:
        name = input("Full Name: ").strip()
        if name:
            break
        print("Name cannot be empty.")
        
    while True:
        email = input("Email Address: ").strip()
        if "@" in email and "." in email:
            break
        print("Please enter a valid email address.")
        
    while True:
        age = input("Age: ").strip()
        if age.isdigit() and int(age) > 0:
            age = int(age)
            break
        print("Please enter a valid age.")
        
    profile = {
        "name": name,
        "email": email,
        "age": age
    }
    return profile

def save_profile(profile, filename="profile.json"):
    # Save the profile to a JSON file with pretty printing.
    with open(filename, "w") as file:
        json.dump(profile, file, indent=4)
    print(f"\nProfile saved successfully to {filename}.")
    
def load_profile(filename="profile.json"):
    # Load the profile from a JSON file.
    if not os.path.exists(filename):
        print("\nNo saved profile found.")
        return None
    
    with open(filename, "r") as file:
        return json.load(file)
    
def display_profile(profile):
    # Display the user profile neatly.
    print("\nSaved User Profile:")
    print("_" * 20)
    for key, value in profile.items():
        print(f"{key.capitalize()}: {value}")
        
def main():
    # Main program flow.
    print("User Profile Manager")
    print("1. Create and save profile")
    print("2. View saved profile")
    
    choice = input("Choose an option (1 or 2): ").strip()
    
    if choice == "1":
        profile = collect_profile()
        save_profile(profile)
    elif choice == "2":
        profile = load_profile()
        if profile:
            display_profile(profile)
    else:
        print("Invalid option selected.")
        
if __name__ == "__main__":
    main()