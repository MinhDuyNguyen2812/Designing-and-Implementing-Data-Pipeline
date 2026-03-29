class TemperatureConverter:
    def __init__(self):
        self.temperature = 0.0

    def setTemperature(self):
        self.temperature += float(input("Enter temperature: "))
        print(f"Temperature set to {self.temperature}")

    def toCelsius(self):
        celcius = self.temperature
        print(f"Temperature in Celcius: {celcius}")
    
    def toFahrenheit(self):
        fahrenheit = (self.temperature * 1.8) + 32
        print(f"Temperature in Fahrenheit: {fahrenheit}")
    
    def toKelvin(self):
        Kelvin = self.temperature + 273.15
        print(f"Temperature in Kelvin: {Kelvin}")
