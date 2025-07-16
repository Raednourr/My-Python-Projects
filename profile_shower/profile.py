import auth
import json
import time


username, logged_in = auth.authenticate()

def show_details():
    with open(auth.accounts_file, "r") as f:
        accounts = json.load(f)


    to_show_details = input("Verify password to show account details: ").strip().lower()
    if to_show_details == accounts[username]["password"]:
        for key, value in accounts[username].items():
            print(f"{key}: {value}")
    else:
        print("Incorrect Password")
    time.sleep(2)


# if logged_in:
#     print(f"Logged in as {username}")
#     show_details()