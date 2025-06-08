"""
Temperature Converter Program - CP1404/CP5632 Practical
Converts temperatures between Celsius and Fahrenheit using a menu system.
"""

# Conversion constants
CELSIUS_TO_FAHRENHEIT_MULTIPLIER = 9 / 5
FAHRENHEIT_TO_CELSIUS_MULTIPLIER = 5 / 9
FAHRENHEIT_FREEZING_POINT = 32

# Menu text
MENU_TEXT = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""

def run_temperature_converter():
    print(MENU_TEXT)
    user_choice = input(">>> ").strip().upper()
    while user_choice != "Q":
        if user_choice == "C":
            temp_celsius = float(input("Enter temperature in Celsius: "))
            temp_fahrenheit = convert_to_fahrenheit(temp_celsius)
            print(f"Temperature in Fahrenheit: {temp_fahrenheit:.2f} F")
        elif user_choice == "F":
            temp_fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            temp_celsius = convert_to_celsius(temp_fahrenheit)
            print(f"Temperature in Celsius: {temp_celsius:.2f} C")
        else:
            print("Invalid selection. Please choose from the menu.")
        print(MENU_TEXT)
        user_choice = input(">>> ").strip().upper()
    print("Exiting the program. Goodbye!")

def convert_to_fahrenheit(celsius_temp):
    """Convert a temperature from Celsius to Fahrenheit."""
    return (celsius_temp * CELSIUS_TO_FAHRENHEIT_MULTIPLIER) + FAHRENHEIT_FREEZING_POINT

def convert_to_celsius(fahrenheit_temp):
    """Convert a temperature from Fahrenheit to Celsius."""
    return (fahrenheit_temp - FAHRENHEIT_FREEZING_POINT) * FAHRENHEIT_TO_CELSIUS_MULTIPLIER

run_temperature_converter()
