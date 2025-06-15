"""
CP1404/CP5632 Practical
Quick Pick Lottery Ticket Generator
"""

import random

NUMBERS_PER_PICK = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

def main():
    quick_picks = int(input("How many quick picks? "))

    for _ in range(quick_picks):
        numbers = []
        while len(numbers) < NUMBERS_PER_PICK:
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
            if number not in numbers:
                numbers.append(number)
        numbers.sort()
        print(" ".join(f"{num:2}" for num in numbers))

main()
