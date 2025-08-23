import json
import os
import time

# variables
menu = """
=== Contact Book Menu ===
1. Add Contact
2. Delete Contact
3. View All Contacts
4. Search Contact
5. Update Contact
6. Exit
"""

contacts_file = "projects/contacts_book/contacts.json"
letters_file = "projects/contacts_book/letters_in_use.json"


def add_contact():
    if os.path.exists(contacts_file) and os.path.getsize(contacts_file):
        with open(contacts_file, "r") as f:
            contacts = json.load(f)
    else:
        contacts = {}
    with open(letters_file, "r") as f:
        letters = json.load(f)

    new_contact_name = input("Enter Contact: ").strip()
    try:
        new_contact_number = int(input("Enter Number: ").strip())
    except ValueError:
        print("Incorrect Value. Closing.")
        return None
    
    new_contact = {new_contact_name: new_contact_number}
    letter = new_contact_name[0].lower()
    if letter not in letters:
        letters.append(letter)
        contacts[letter] = []

    contacts[letter].append(new_contact)

    with open(contacts_file, "w") as f:
        json.dump(contacts, f, indent=4)

    with open(letters_file, "w") as f:
        json.dump(letters, f, indent=4)
    time.sleep(0.35)
    print("Added Contact Succesfully!")

while True:
    print(menu)

    choice = input("Enter choice (1-6): ").strip()

    if choice == "6":
        print("Exiting...")
        time.sleep(0.5)
        break
    elif choice == "1":
        add_contact()
        time.sleep(1)
    elif choice == "2":
        time.sleep(1)
    elif choice == "3":
        time.sleep(1)
    elif choice == "4":
        time.sleep(1)
    elif choice == "5":
        time.sleep(1)
    else:
        print("Ivalid choice!")
        time.sleep(1)
        continue