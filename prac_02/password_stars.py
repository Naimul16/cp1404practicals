

MIN_LENGTH = 8  # minimum password length

def main():

    password = get_password()

    print_asterisks(password)


def print_asterisks(password):
    print("*" * len(password))


def get_password():
    password = input("Enter your password: ")
    while len(password) < MIN_LENGTH:
        print(f"Password too short! It must be at least {MIN_LENGTH} characters.")
        password = input("Enter your password: ")
    return password


main()