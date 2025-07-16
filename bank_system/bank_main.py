import bank_auth
import bank_systems

account = bank_auth.authorize()

if bank_auth.account_logged:
    print(f"Welcome {account}!")
    bank_systems.bank_functions(account)
else:
    print("No account logged in.")