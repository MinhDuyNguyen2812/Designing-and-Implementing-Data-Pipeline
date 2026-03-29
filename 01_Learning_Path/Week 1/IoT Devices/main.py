from file_handler import FileHandler
from device import Device, TemperatureSensor, HumiditySensor, MotionSensor

filename = "data.csv"
data_file = FileHandler(filename)
rows = data_file.read()
devices = [Device.deserialize(row) for row in rows if row.strip() != ""]

def showOptions():
    print(f"Menu:")
    print(f"1 - Add IoT Device")
    print(f"2 - Serialize Data")
    print(f"3 - Deserialize Data")
    print(f"4 - Encrypt Data")
    print(f"5 - Decrypt Data")
    print(f"0 - Exit")
    choice = input("Choice: ")
    return choice

def showDevicesMenu():
    print(f"1 - Temperature Sensor")
    print(f"2 - Humidity Sensor")
    print(f"3 - Motion Sensor")
    print(f"0 - Back")
    choice = input("Device type: ")
    return choice

def add_device():
    while True:
        choice = showDevicesMenu()
        try:
            choice = int(choice)
        except ValueError:
            print(f"Invalid choice.")
            continue

        deviceId = input("Device ID: ")
        location = input("Location: ")
        data = input("Data: ")
        if choice == 1:
            device = TemperatureSensor(deviceId, location, data)
        elif choice == 2:
            device = HumiditySensor(deviceId, location, data)
        elif choice == 3:
            device = MotionSensor(deviceId, location, data)
        elif choice == 0:
            break
        else:
            print(f"Invalid choice.")
            continue
        devices.append(device)
        data_file.write([d.serialize() for d in devices])

def serialize_data():
    for device in devices:
        row = device.serialize()
        print(row)

def deserialize_data():
    for device in devices:
        print(f"{device.deviceId}, {device.location}, {device.data}")

def main():
    while True:
        choice = showOptions()
        try:
            choice =int(choice)
        except ValueError:
            print(f"Invalid choice.")
            continue

        if choice == 1:
                add_device()
        elif choice == 2:
            serialize_data()
        elif choice == 3:
            deserialize_data()
        elif choice == 4:
            pass
        elif choice == 5:
            pass
        elif choice == 0:
            print(f"Exiting...\n")
            break

if __name__ == "__main__":
    main()
