
# GLOBAL VARIABLES :
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# FUNCTION TO CONVERT FROM FAHRENHEIT TO CELSIUS :
def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    celsius = FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32)
    print(f"{fahrenheit}°F is {celsius}°C")

# FUNCTION TO CONVERT FROM CELSIUS TO FAHRENHEIT :
def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    fahrenheit = (CELSIUS_TO_FAHRENHEIT_FACTOR * celsius) + 32
    print(f"{celsius}°C is {fahrenheit}°F")

while True:
    try:
        user_input = input('Enter the temperature to convert: ')
        user_input = float(user_input)
        break
    except:
        print("Invalid temperature. Please enter a numeric value.")
    
unit_check = input('Is this temperature in Celsius or Fahrenheit? (C/F): ').capitalize()
while unit_check not in ('C', 'F'):
    unit_check = input('Is this temperature in Celsius or Fahrenheit? (C/F): ').capitalize()

if unit_check == 'C':
    convert_to_fahrenheit(user_input)
else:
    convert_to_celsius(user_input)

