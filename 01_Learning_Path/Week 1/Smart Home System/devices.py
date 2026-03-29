from smart_device import SmartDevice

class SmartLight(SmartDevice):
    def __init__(self, deviceName, status, brightness):
        super().__init__(deviceName, status)
        self.brightness = brightness

    def operate(self):
        print(f"Light {self.deviceName} is {self.status} with brightness {self.brightness}")

class SmartThermostat(SmartDevice):
    def __init__(self, deviceName, status, temperature):
        super().__init__(deviceName, status)
        self.temperature = temperature

    def operate(self):
        print(f"Thermostat {self.deviceName} set to {self.temperature}°C")

class SmartLock(SmartDevice):
    def __init__(self, deviceName, status, locked):
        super().__init__(deviceName, status)
        self.locked = locked

    def operate(self):
        print(f"Lock {self.deviceName} is {'locked' if self.locked else 'unlocked'}")