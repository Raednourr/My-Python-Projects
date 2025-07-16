import json
import os
import time

security_file = "projects/student_gradebook/security.json"

def login():
    if os.path.exists(security_file) and os.path.getsize(security_file) > 0:
            with open(security_file, "r") as f:
                security = json.load(f)
    else:
        security = {}

    print("AUTHENTICATION")
    print("")
    tries = 0

    for attempt in range(3):
        password = input("Enter authentication password: ").strip().lower()
        if password == security["password"].lower():
            print("Entering Gradebook...")
            return True
        else:
            print("Incorrect Password")
    print("Too many attempts, closing...")
    return False

    # with open(security_file, "w") as f:
    #      json.dump(security, f, indent=2)

# login()