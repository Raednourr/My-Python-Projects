import json
import os
import time

usersfile = "Power_Usage_Tracker/users.json"
devises_file = "Power_Usage_Tracker/devices.json"
account_username = ""
account_logged = False

def register():
    if os.path.exists(usersfile) and os.path.getsize(usersfile) > 0:
        with open(usersfile, "r") as f:
            users: dict[str, str] = json.load(f)
    
    else:
        users: dict[str, str] = {}

    if os.path.exists(usersfile) and os.path.getsize(usersfile) > 0:
        with open(devises_file, 'r') as f:
            devices = json.load(f)
    else:
        devices = {}
    
    

    username = input('Enter username: ').strip().lower()
    if username in users:
        print("Username taken")
        return None, False
    password = input('Enter Password: ').strip()
    users[username] = password
    account_logged = True
    account_username = username
    print("DEBUG " ,account_username)
    print("DEBUG ", account_logged)
    rate = float(input("Enter your rate/kwh: ").strip())
    devices[username] = {
        "rate_per_kwh": rate,
        "devices": {}
    }
    with open(usersfile, "w") as f:
        json.dump(users, f, indent=4)
    with open(devises_file, "w") as f:
        json.dump(devices, f, indent=4)
    return username, True


def log_in():
    with open(usersfile, "r") as f:
        users = json.load(f)

    wanted_username = input("Enter username: ").strip().lower()
    wanted_password = input("Enter password: ").strip()

    if wanted_username in users and users[wanted_username] == wanted_password:
        # print(f"Logging in as {wanted_username}")
        account_logged = True
        account_username = wanted_username
        return account_username, True
    else:
        print("Incorrect username or password")
        return None, False

def authenticate():
    authentication = input("LogIn (l) or Register account (r): ").strip().lower()

    if authentication == "l":
        return log_in()
        # time.sleep(1)
    elif authentication == "r":
        return register()
        # time.sleep(1)
    else:
        print("Not a valid choice!")
        return None, False
    
# authenticate()