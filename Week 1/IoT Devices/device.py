from dataclasses import dataclass

@dataclass
class Device:
    SEPARATOR = ","
    deviceId: str
    location: str
    data: str

    def toList(self):
        return [self.__class__.__name__, self.deviceId, self.location, self.data]

    @staticmethod
    def deserialize(row):
        columns = [c.strip() for c in row.split(Device.SEPARATOR)]
        class_name, deviceId, location, data = columns

        if class_name == "TemperatureSensor":
            return TemperatureSensor(deviceId, location, data)
        elif class_name == "HumiditySensor":
            return HumiditySensor(deviceId, location, data)
        elif class_name == "MotionSensor":
            return MotionSensor(deviceId, location, data)
        else:
            return Device(deviceId, location, data)


    def serialize(self):
        return self.SEPARATOR.join([self.__class__.__name__, str(self.deviceId), str(self.location), str(self.data)])

    def set_new_data(self, new_data):
        self.data = new_data

class TemperatureSensor(Device):
    pass

class HumiditySensor(Device):
    pass

class MotionSensor(Device):
    pass
