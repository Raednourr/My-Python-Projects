import json
import os
import time


menu = """
    --- 📝 TASK PLANNER MENU ---

1. Add new task
2. View my tasks
3. Mark task as completed
4. Edit a task
5. Delete a task
6. Log out

"""

users_file = "task_planner/users.json"
tasks_file = "task_planner/tasks.json"

def add_task(user):
    # 🔍 Step 1: Check if the file exists and is not empty
    if os.path.exists(tasks_file) and os.path.getsize(tasks_file) > 0:
        # 🧠 If yes, open it and load all tasks into a Python dictionary
        with open(tasks_file, "r") as f:
            tasks = json.load(f)
    else:
        # 🧠 If the file doesn’t exist or is empty, start with an empty dictionary
        tasks = {}

    # 🔑 Step 2: Make sure the current user has a task list
    if user not in tasks:
        tasks[user] = []  # Start an empty task list for this user

    # 📝 Step 3: Ask the user for a new task name
    task_name = input("Enter task: ").strip()  # Remove extra spaces

    # 🧱 Step 4: Create the new task as a dictionary
    new_task = {"Task": task_name, "Done": False}

    # 📌 Step 5: Add the new task to this user’s task list
    tasks[user].append(new_task)

    # 💾 Step 6: Save the updated tasks back into the JSON file
    with open(tasks_file, "w") as f:
        json.dump(tasks, f, indent=4)

    # ✅ Step 7: Show a confirmation message
    print("✅ Task added.")

def view_tasks(account):
    with open(tasks_file, "r") as f:
        tasks = json.load(f)
    for task in tasks[account]:
        print(task["Task"], task["Done"])


def mark_task(account):
    with open(tasks_file, "r") as f:
        tasks = json.load(f)

    print("Account:", account)  # Debug
    # print("All tasks loaded:", tasks)  # Debug

    if account in tasks:
        print(f"✅ Tasks for {account}:")
        for task in tasks[account]:
            print("- " + task["Task"])
        taske = input("Enter task name: ").strip()
        if taske == task["Task"]:
            task["Done"] = True
    
    else:
        print("⚠️ No tasks found for this account.")

    with open(tasks_file, "w") as f:
        json.dump(tasks, f, indent=4)
    print("Task Marked!")
def edit_task(account):
    with open(tasks_file, "r") as f:
        tasks = json.load(f)
    for task in tasks[account]:
        print(f"-{task["Task"]}, {task["Done"]}")
    wanted_task = input("Enter task name: ")
    for task in tasks[account]:
        if wanted_task == task["Task"]:
            new_task = input("Edit: ")
            task["Task"] = new_task
    
    with open(tasks_file, "w") as f:
        json.dump(tasks, f, indent=4)
    print("Task Edited!")
def delete_task(account):
    with open(tasks_file, "r") as f:
        tasks = json.load(f)
    for task in tasks[account]:
        print(f"-{task["Task"]}, {task["Done"]}")
    wanted_task = input("Enter task name: ")
    for task in tasks[account]:
        if wanted_task == task["Task"]:
            tasks[account].remove(task)
    
    with open(tasks_file, "w") as f:
        json.dump(tasks, f, indent=4)
    print("Task deleted!")



def tasks_functionality(user):
    while True:
        print(menu)
        choice = input("Enter (1-6): ").strip().lower()
        if choice == "6":
            break
        elif choice == "1":
            add_task(user)
            time.sleep(1.5)
        elif choice == "2":
            view_tasks(user)
            time.sleep(1.5)
        elif choice == "3":
            mark_task(user)
            time.sleep(1.5)
        elif choice == "4":
            edit_task(user)
            time.sleep(1.5)
        elif choice == "5":
            delete_task(user)
            time.sleep(1.5)
        else:
            print("Not a choice!")


