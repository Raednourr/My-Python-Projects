from auth import functionality
from task_manager import *

def main():

    user = functionality()  # Handle login or register

    if user:
        print("📝 Welcome to the Task Planner 📝")
        print(f"\n🔓 Welcome, {user}!")
        tasks_functionality(user) 
    else:
        print("⚠️ No account logged in. Exiting...")

if __name__ == "__main__":
    main()
