FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    C = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return C

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    F = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return F

while True:
    temperature = input('Enter the temperature to convert: ')
    try:
        temperature = float(temperature)
        break
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").capitalize()
while unit not in ("C", "F"):
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").capitalize()

if __name__ == '__main__':
    if unit == 'F':
        converted = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted}°C")
    else:
        converted = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted}°F")