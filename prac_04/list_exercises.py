"""
CP1404/CP5632 Practical
Working with lists: getting user input, calculating stats, and checking user access
"""

def main():
    # Section 1 – Gathering numbers and showing stats
    user_numbers = []

    for count in range(5):
        entered_number = int(input("Enter a number: "))
        user_numbers.append(entered_number)

    print(f"The first number is {user_numbers[0]}")
    print(f"The last number is {user_numbers[-1]}")
    print(f"The smallest number is {min(user_numbers)}")
    print(f"The largest number is {max(user_numbers)}")
    print(f"The average is {sum(user_numbers) / len(user_numbers)}")

    # Section 2 – Verifying username access
    approved_users = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
                      'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
                      'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

    login_name = input("Username: ")
    if login_name in approved_users:
        print("Access granted")
    else:
        print("Access denied")


main()
