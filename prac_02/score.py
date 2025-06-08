"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    try:
        score = float(input("Enter score: "))
        result = evaluate_score(score)
        print(result)
        random_score()
    except ValueError:
        print("Invalid input! Please enter a number.")


def evaluate_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    else:
        return "Bad"


def random_score():
    number = random.randint(0, 100)
    print(number)
    score = evaluate_score(number)
    print(score)

main()
