from temperature_converter import TemperatureConverter

def showOptions():
    print(f"Options: ")
    print(f"1) Set temperature")
    print(f"2) Convert to Celsius")
    print(f"3) Convert to Fahrenheit")
    print(f"4) Convert to Kelvin")
    print(f"0) Exit program")
    Choice = int(input("Choice: "))
    return Choice

def main():
    converter = TemperatureConverter()
    print(f"Program starting.")
    print(f"Initializing temperature converter...")
    print(f"Temperature converter initialized.")
    print()

    while True:
        choice = showOptions()
        
        
        if choice == 1:
            converter.setTemperature()
            print()
        elif choice == 2:
            converter.toCelsius()
            print()
        elif choice == 3:
            converter.toFahrenheit()
            print()
        elif choice == 4:
            converter.toKelvin()
            print()
        elif choice == 0:
            print(f"Program ending.")
            break
        else:
            print(f"Unknown option!")

if __name__ == "__main__":
    main()