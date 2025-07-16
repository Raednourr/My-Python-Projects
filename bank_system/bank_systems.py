import json
import os
import time
from bank_auth import account

users_file = "bank_system/bank_users.json"
balance_file = "bank_system/accounts.json"

menu = """
🏦 Bank Menu
───────────────
1. 💰 Deposit
2. 🧾 Withdraw
3. 📄 View Balance
4. 🕓 Transaction History
5. 🚪 Logout
"""

class Bank:
    
    def __init__(self, account_logged_in):
        self.account = account_logged_in

    def deposit(self):
        
        with open(users_file, "r") as f:
            users = json.load(f)
        with open(balance_file, "r") as f:
            balances = json.load(f)
        # if account_logged_in not in balances:
        #     print("❌ Account not found.")
        #     return
        amount_deposisted = int(input("Enter amount: "))
        if amount_deposisted <= 0:
            print("Choose a higher number than 0!")
        balances[self.account] += amount_deposisted
        print(f"✅ Deposited {amount_deposisted}. New balance: {balances[self.account]}")
        with open(balance_file, "w") as f:
            json.dump(balances, f, indent=4)

    def withdraw(self):
        with open(balance_file, "r") as f:
            balances = json.load(f)

        ammount_withdrawed = int(input("Enter Amount: "))
        if ammount_withdrawed <= balances[self.account] and ammount_withdrawed > 0:
            balances[self.account] -= ammount_withdrawed
            print(f"Ammount witdrawed: {ammount_withdrawed}")
            print(f"Ammount left in account: {balances[self.account]}")

        else:
            print("Ammount higher than account ballance or lower than 0: ")
        
        with open(balance_file, "w") as f:
            json.dump(balances, f, indent=4)
    
    def view_balance(self):
        with open(balance_file, "r") as f:
            balances = json.load(f)

        balance = balances[self.account]
        print(f"Account balance: {balance}")
            


def bank_functions(account):
    bank = Bank(account)
    while True:
        print(menu)
        choice = input("Choose (1-5): ")
        if choice == "5":
            break
        elif choice == "1":
            bank.deposit()
            time.sleep(1.5)
        elif choice == "2":
            bank.withdraw()
            time.sleep(1.5)

        elif choice == "3":
            bank.view_balance()
            time.sleep(1.5)

        elif choice == "4":
            print("Workin on it")
            time.sleep(1.5)
        
        else:
            print("Not a choice")
