"""
Hex Code Finder
Retrieve hexadecimal color codes using a name-based dictionary
"""

HEX_CODES = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aqua": "#00ffff",
    "aquamarine": "#7fffd4",
    "azure": "#f0ffff",
    "beige": "#f5f5dc",
    "black": "#000000",
    "blueviolet": "#8a2be2",
    "brown": "#a52a2a",
    "burlywood": "#deb887"
}

user_colour = input("Enter a colour name: ").lower()
while user_colour != "":
    try:
        print(f"The code for {user_colour} is {HEX_CODES[user_colour]}")
    except KeyError:
        print("Invalid colour name")
    user_colour = input("Enter a colour name: ").lower()
