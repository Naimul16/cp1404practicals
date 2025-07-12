"""
Email Contacts
Estimate: 45 minutes
Actual:   60 minutes
"""

def extract_full_name(address):
    """Derive full name from an email string."""
    username_parts = address.split('@')[0].split('.')
    full_name = ' '.join(username_parts).title()
    return full_name

def run_program():
    """Collect email addresses and names in a dictionary, then print them."""
    contacts = {}
    user_email = input("Email: ")
    while user_email != "":
        default_name = extract_full_name(user_email)
        response = input(f"Is your name {default_name}? (Y/n) ").strip().lower()
        if response != "" and response != "y":
            default_name = input("Name: ").strip()
        contacts[user_email] = default_name
        user_email = input("Email: ")

    print()
    for address, person in contacts.items():
        print(f"{person} ({address})")

run_program()
