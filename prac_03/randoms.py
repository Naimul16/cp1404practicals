import random

# Line 1: random.randint(5, 20)
# This generates a random integer between 5 and 20 (inclusive).
# Example outputs seen: 13, 7, 20
# Smallest seen: 5
# Largest seen: 20
print(random.randint(5, 20))

# Line 2: random.randrange(3, 10, 2)
# This generates a random number from the range 3 to 9, stepping by 2.
# Possible values: 3, 5, 7, 9 (all odd numbers in range)
# Example outputs seen: 3, 5, 9
# Smallest seen: 3
# Largest seen: 9
# Could this produce a 4? → No, because 4 is not part of the step sequence.
print(random.randrange(3, 10, 2))

# Line 3: random.uniform(2.5, 5.5)
# This generates a floating-point number between 2.5 and 5.5.
# Example outputs seen: 3.42, 4.98, 2.76
# Smallest seen: ~2.5
# Largest seen: ~5.5
print(random.uniform(2.5, 5.5))

# Task: Write code to produce a random number between 1 and 100 inclusive
random_number = random.randint(1, 100)
print(random_number)
