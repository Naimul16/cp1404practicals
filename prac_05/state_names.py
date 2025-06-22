"""
CP1404/CP5632 Practical
Australian state lookup using abbreviations
"""

ABBREVIATION_TO_STATE = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania",
    "SA": "South Australia"
}

print("Available state codes and their full names:")
for abbrev, full_name in ABBREVIATION_TO_STATE.items():
    print(f"{abbrev:>3} is {full_name}")

print()

user_input = input("Enter a state code: ").upper()
while user_input != "":
    try:
        result = ABBREVIATION_TO_STATE[user_input]
        print(f"{user_input} is {result}")
    except KeyError:
        print("Invalid state code")
    user_input = input("Enter a state code: ").upper()
