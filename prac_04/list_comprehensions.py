"""
CP1404/CP5632 Practical
Working with List Comprehensions
"""

short_names = ["Bob", "Angel", "Jimi", "Alan", "Ada"]
complete_names = ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing", "Ada Lovelace"]

# Create a list of first letters from each name using a for loop
initial_letters = []
for person in short_names:
    initial_letters.append(person[0])
print(initial_letters)

# Same as above but using a list comprehension
initial_letters = [person[0] for person in short_names]
print(initial_letters)

# Create a list of initials (first and last) from the full names
name_initials = [full.split()[0][0] + full.split()[1][0] for full in complete_names]
print(name_initials)

# Filter names that begin with 'A'
names_starting_with_a = [person for person in short_names if person.startswith('A')]
print(names_starting_with_a)

# Display all names in alphabetical order, joined as one string
print(" ".join(sorted(short_names)))

# TODO: Make all full names lowercase
full_names_lower = [entry.lower() for entry in complete_names]
print(full_names_lower)

raw_numbers = ['0', '10', '21', '3', '-7', '88', '9']

# TODO: Convert string numbers to integers
converted_numbers = [int(value) for value in raw_numbers]
print(converted_numbers)

# TODO: Filter numbers greater than 9
filtered_numbers = [val for val in converted_numbers if val > 9]
print(filtered_numbers)

# TODO: Extract last names from full names longer than 11 characters
# Output: 'Harlem, Hendrix, Lovelace'
long_last_names = ", ".join([entry.split()[1] for entry in complete_names if len(entry) > 11])
print(long_last_names)
