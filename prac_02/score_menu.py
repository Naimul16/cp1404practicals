import random

# Constants
MIN_SCORE = 0
MAX_SCORE = 100
PASS_THRESHOLD = 50
EXCELLENT_THRESHOLD = 90

MENU = """(G)et a valid score (must be 0-100 inclusive)
(P)rint result (copy or import your function to determine the result from score.py)
(S)how stars (this should print as many stars as the score)
(Q)uit"""

def main():
    print(MENU)
    choice = input(">>> ").strip().upper()
    current_score = 0
    while choice != "Q":
        if choice == "G":
            current_score = get_random_score()
            print(f"Generated Score: {current_score}")
        elif choice == "P":
            user_score = float(input("Enter a score: "))
            result = evaluate_score(user_score)
            print(f"Result: {result}")
        elif choice == "S":
            print_stars(current_score)
        else:
            print("Invalid selection. Please choose again.")
        print(MENU)
        choice = input(">>> ").strip().upper()
    print("Thank you for using the program.")

def evaluate_score(score):
    """Return the evaluation of the score based on thresholds."""
    if score < MIN_SCORE or score > MAX_SCORE:
        return "Invalid score"
    elif score > EXCELLENT_THRESHOLD:
        return "Excellent"
    elif score > PASS_THRESHOLD:
        return "Passable"
    else:
        return "Bad"

def print_stars(score):
    """Print asterisks representing the score."""
    print("*" * int(score))

def get_random_score():
    """Generate and return a random score between MIN_SCORE and MAX_SCORE."""
    return random.randint(MIN_SCORE, MAX_SCORE)

main()
