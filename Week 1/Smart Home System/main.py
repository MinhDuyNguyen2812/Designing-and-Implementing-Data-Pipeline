from devices import SmartLight, SmartThermostat, SmartLock
from device_controller import operate_devices

devices = []

def show_menu():
    print("\nMenu:")
    print("1 - Add Smart Device")
    print("2 - Operate Devices")
    print("0 - Exit")

def add_device():
    print("\nDevice type:")
    print("1 - Smart Light")
    print("2 - Smart Thermostat")
    print("3 - Smart Lock")

    choice = input("Choice: ")

    name = input("Device name: ")
    status = input("Status (on/off): ")

    if choice == "1":
        brightness = input("Brightness: ")
        devices.append(SmartLight(name, status, brightness))
    elif choice == "2":
        temperature = input("Temperature: ")
        devices.append(SmartThermostat(name, status, temperature))
    elif choice == "3":
        locked = input("Locked (yes/no): ")
        locked = True if locked.lower() == "yes" else False
        devices.append(SmartLock(name, status, locked))
    else:
        print("Invalid device type")

def main():
    while True:
        show_menu()
        choice = input("Choice: ")

        if choice == "1":
            add_device()
        elif choice == "2":
            operate_devices(devices)
        elif choice == "0":
            print("Exit")
            break
        else:
            print("Invalid menu choice")

if __name__ == "__main__":
    main()