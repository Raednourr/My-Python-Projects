import json
import os

USERS_FILE = "task_planner/users.json"

def functionality() -> str | None:
    # 🔁 Load accounts as a dictionary {username: password}
    if os.path.exists(USERS_FILE) and os.path.getsize(USERS_FILE) > 0:
        with open(USERS_FILE, "r") as f:
            accounts: dict[str, str] = json.load(f)
    else:
        accounts: dict[str, str] = {}

    choice = input("Login (l) or Register (r): ").strip().lower()

    # 🔐 LOGIN
    if choice == "l":
        username = input("Enter username: ").strip().lower()
        password = input("Enter password: ")
        if accounts.get(username) == password:
            print(f"✅ Logged in as {username}")
            return username
        else:
            print("❌ Incorrect username or password.")
            return None

    # ✍️ REGISTER
    elif choice == "r":
        username = input("Choose a username: ").strip().lower()
        if username in accounts:
            print("❌ Username already taken.")
            return None
        password = input("Choose a password: ")
        accounts[username] = password  # ✅ Save directly

        with open(USERS_FILE, "w") as f:
            json.dump(accounts, f, indent=4)

        print(f"✅ Registered and logged in as {username}")
        return username

    else:
        print("❌ Not a valid choice.")
        return None
