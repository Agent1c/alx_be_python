FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    while True:
        temperature = float(input("Enter the temperature: "))
        unit = input("Enter the unit (F or C): ").capitalize()

        match unit:
            case _ if unit.capitalize() == "F":
              print(f"{temperature}°F is equal to {convert_to_celsius(temperature):.2f}°C")
            case _ if unit.capitalize() == "C":
                print(f"{temperature}°C is equal to {convert_to_fahrenheit(temperature):.2f}°F")
            case _ :
                print(("Invalid temperature unit. Please enter F or C."))
                break

if __name__ == "__main__":
    main()