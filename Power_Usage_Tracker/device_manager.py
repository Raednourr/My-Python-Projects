import json
import os
import time
import auth

users_file = "Power_Usage_Tracker/users.json"
devises_file = "Power_Usage_Tracker/devices.json"


class PowerTracker:

    def __init__(self, account_logged):
        self.account = account_logged

    def add_device(self):
        with open(devises_file, "r") as f:
            devices = json.load(f)

        device = input("Enter device: ").strip()
        watt = input("Enter device Watt: ")
        duration = input("Enter time used: ")


        devices[self.account]["devices"][device] = {
            "wattage": watt,
            "time_used": duration        
        }

        with open(devises_file, "w") as f:
            json.dump(devices, f, indent=4)

    def view_devices(self):
        with open(devises_file, "r") as f:
            devices = json.load(f)

        for device in devices[self.account]["devices"]:
            print(device)

    def calc_cost(self):
        with open(devises_file, "r") as f:
            devices = json.load(f)
        user_rate = devices[self.account]["rate_per_kwh"]
        costs = []
        for device_name, device_info in devices[self.account]["devices"].items():
            device_watt = int(device_info["wattage"])
            device_usage = int(device_info["time_used"])
            energy_used = (device_watt * device_usage) / 1000 
            cost = energy_used * user_rate
            print(f"cost of {device_name} = {cost}")
            costs.append(cost)
        print(f"Total cost: {sum(costs)}")
        
    # hello

# power = PowerTracker()
        

