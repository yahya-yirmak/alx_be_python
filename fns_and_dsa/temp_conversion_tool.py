FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    return FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32)

def convert_to_fahrenheit(celsius):
    return (CELSIUS_TO_FAHRENHEIT_FACTOR * celsius) + 32

def user_interaction():
    while True:
        try:
            temperature_input = input("Enter the temperature to convert: ")
            temperature = float(temperature_input)
            break 
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")
    
    while True:
        scale = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        if scale in ('C', 'F'):
            break
        else:
            print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    
    if scale == 'C':
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted_temp}°F")
    else:
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted_temp}°C")

def main():
    user_interaction()

if __name__ == "__main__":
    main()
