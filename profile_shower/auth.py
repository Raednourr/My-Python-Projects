import os
import json
import time

accounts_file = "projects/profile_shower/accounts.json"

def register():
    if os.path.exists(accounts_file) and os.path.getsize(accounts_file) > 0:
        with open(accounts_file, "r") as f:
            accounts = json.load(f)
    else:
        accounts = {}

    current_year = 2025
    what_allergy = None
    name = input("Enter Name (No special characters): ").strip()
    if name in accounts:
        print("Name taken.")
        return None, False
    elif not name.isalpha():
        print("Invalid name (Contains special characters).")
        return None, False
    try:
        birth_year = int(input("Enter birth year: ").strip())
        if birth_year > current_year:
            print("Invalid birth year.")
            return None, False
    except ValueError:
        print("Enter valid year (No Letters).")
        return None, False
    password = input("Enter password: ").strip().lower()
    allergies = input("Any allergies? (y, n): ").strip().lower()
    if allergies == "y":
        what_allergy = input("Enter Allergies: ")
    else:
        what_allergy = None
    new_account_details = {
        "age": current_year - birth_year,
        "birth year": birth_year,
        "password": password,
        "Allergies": what_allergy
    }
    

    accounts[name] = new_account_details


    with open(accounts_file, "w") as f:
        json.dump(accounts, f, indent=4)

    return name, True


def log_in():
    with open(accounts_file, "r") as f:
        accounts = json.load(f)

    username = input("Enter name: ").strip()
    password = input("Enter password: ").strip().lower()

    if username in accounts and accounts[username]["password"] == password:
        # print(f"Logging in as {username}")
        return username, True
    else:
        print("Incorrect username or password.")
        return None, False

def authenticate():
    choice = input("LogIn (l) or Register (r): ").strip().lower()

    if choice == "l":
        return log_in()
    elif choice == "r":
        return register()

    else:
        print("Not an option! Try again.")

# authenticate()