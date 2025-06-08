"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    - A ValueError will occur if the user enters something that cannot be converted to an integer,
      such as a letter or a special character (e.g., 'a', '12.5', '%').

2. When will a ZeroDivisionError occur?
    - A ZeroDivisionError will occur if the user enters 0 for the denominator.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    - Yes. By using a while loop to repeatedly ask for the denominator until the user provides a non-zero value.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator (non-zero): "))
    while denominator == 0:
        print("Denominator cannot be zero.")
        denominator = int(input("Enter the denominator (non-zero): "))
    fraction = numerator / denominator
    print(f"Result: {fraction}")
except ValueError:
    print("Numerator and denominator must be valid integers!")
print("Finished.")
