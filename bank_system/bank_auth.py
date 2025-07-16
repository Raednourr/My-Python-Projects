import json
import os


user_file = "bank_system/bank_users.json"
balance_file = "bank_system/accounts.json"
account_logged = False
account = ""

class User:

    def login(self):
        global account_logged
        global account
        with open(user_file, "r") as f:
            users: dict[str, str] = json.load(f)
        wanted_name = input("Enter username: ")
        wanted_password = input("Enter password: ")

        for username, pw in users.items():
            if pw == wanted_password and username == wanted_name:
                account = username
                account_logged = True
                print(f"[DEBUG]: {account_logged}") 
                print(f"[DEBUG]: {account}")
                print("Logging in!")
                return username
        if not account_logged:         
            print("Account not found.")
    

    def register(self):
        global account_logged
        global account
        
        if os.path.exists(user_file) and os.path.getsize(user_file) > 0:
            with open(user_file, "r") as f:
                users: dict[str, str] = json.load(f)
        else:
            users: dict[str,str] = {}

        if os.path.exists(balance_file) and os.path.getsize(balance_file) > 0:
            with open(balance_file, "r") as f:
                balances: dict[str, str] = json.load(f)
        else: 
            balances: dict[str, str] = {}

        username = input("Enter username: ").strip()
        if username in users:
            print("Username used")
            return None
        password = input("Enter password: ").strip()
        users[username] = password
        account_logged = True
        account = username
        print(account_logged) 
        print(account)
        for usernamee, pw in users.items():
            if usernamee == account:
                print(f"Logged In as {usernamee}!")
                balance = int(input("Enter balance: "))
                balances[usernamee] = balance
                return username
        try:
            with open(user_file, "w") as f:
                json.dump(users, f, indent=4)
            with open(balance_file, "w") as f:
                json.dump(balances, f, indent=4)
        except Exception as e:
            print("Error in saving files")
        


def authorize():
    user = User()
    auth = input("Register (r) or Login (l): ").strip().lower()
    if auth == "r":
        return user.register()
    elif auth == "l":
        return user.login()
    else:
        print("Not a choice")
        return None

# authorize()











