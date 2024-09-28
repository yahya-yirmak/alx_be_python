
# GLOBAL VARIABLES :
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# FUNCTION TO CONVERT FROM FAHRENHEIT TO CELSIUS :
def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32)

# FUNCTION TO CONVERT FROM CELSIUS TO FAHRENHEIT :
def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (CELSIUS_TO_FAHRENHEIT_FACTOR * celsius) + 32

if __name__ == '__main__':

    while True:
        user_input = input('Enter the temperature to convert: ')
        try:
            user_input = float(user_input)
            break
        except:
            print("Invalid temperature. Please enter a numeric value.")
    
    unit = input('Is this temperature in Celsius or Fahrenheit? (C/F): ').capitalize()
    while unit not in ('C', 'F'):
        unit = input('Is this temperature in Celsius or Fahrenheit? (C/F): ').capitalize()

    if unit == 'C':
        fahrenheit = convert_to_fahrenheit(user_input)
        print(f"{user_input}°C is {fahrenheit}°F")
    else:
        celsius = convert_to_celsius(user_input)
        print(f"{user_input}°F is {celsius}")



FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


def convert_to_celsius(fahrenheit):
    return FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32)


def convert_to_fahrenheit(celsius):
    return (CELSIUS_TO_FAHRENHEIT_FACTOR * celsius) + 32

if __name__ == '__main__':
    while True:
        user_input = input('Enter the temperature to convert: ')
        try:
            user_input = float(user_input)
            break
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")
    
    unit = input('Is this temperature in Celsius or Fahrenheit? (C/F): ').capitalize()
    while unit not in ('C', 'F'):
        unit = input('Is this temperature in Celsius or Fahrenheit? (C/F): ').capitalize()

    if unit == 'C':
        fahrenheit = convert_to_fahrenheit(user_input)
        print(f"{user_input}°C is {fahrenheit:.2f}°F")
    else:
        celsius = convert_to_celsius(user_input)
        print(f"{user_input}°F is {celsius:.2f}°C")

