# CP1404/CP5632 - Practical
# File reading and writing tasks with no magic numbers

# Constants
NAME_FILE = 'name.txt'
NUMBERS_FILE = 'numbers.txt'
FIRST_INDEX = 0
SECOND_INDEX = 1

# 1. Ask the user for their name and write it to 'name.txt' using open and close
user_name = input("Enter your name: ")
output_file = open(NAME_FILE, 'w')
output_file.write(user_name)
output_file.close()

# 2. Read the name from 'name.txt' and greet the user
input_file = open(NAME_FILE, 'r')
stored_name = input_file.read().strip()
input_file.close()
print(f"Hi {stored_name}!")

# 3. Read the first two numbers from 'numbers.txt', add them and print the result
with open(NUMBERS_FILE, 'r') as file:
    all_lines = file.readlines()
    first_number = int(all_lines[FIRST_INDEX])
    second_number = int(all_lines[SECOND_INDEX])
    sum_first_two = first_number + second_number
    print(f"Sum of first two numbers: {sum_first_two}")

# 4. Read all numbers from 'numbers.txt', sum them and print the total
with open(NUMBERS_FILE, 'r') as file:
    total_sum = 0
    for line in file:
        total_sum += int(line.strip())
    print(f"Total of all numbers: {total_sum}")
