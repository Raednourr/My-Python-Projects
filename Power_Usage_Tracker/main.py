import auth
import device_manager

username, logged_in = auth.authenticate()

if logged_in:
    print(f"Logged In as {username}")
    menu = """
    Welcome to Power Tracker

    1. Add a device
    2. View devices
    3. View cost
    4. Save and exit

    """
    while True:
        power_tracker = device_manager.PowerTracker(username)
        choice = input("Pick (1-4): ")
        if choice == "4":
            break
        elif choice == "1":
            power_tracker.add_device()
        elif choice == "2":
            power_tracker.view_devices()
        elif choice == "3":
            power_tracker.calc_cost()

else:
    print("No account logged in")