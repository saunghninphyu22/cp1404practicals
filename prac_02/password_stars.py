"""Module to validate password length and display asterisks."""

MAX_LENGTH = 15
MIN_LENGTH = 3

def main():
    """Main function to manage password input and display."""
    password = get_password()
    print_asterisks(password)

def get_password():
    """Prompt the user for a valid password and return it."""
    password = input("What is the password?: ")
    while len(password) > MAX_LENGTH or len(password) < MIN_LENGTH:
        print(f"Password must be between {MIN_LENGTH} and {MAX_LENGTH} characters.")
        password = input("What is the password?: ")
    return password

def print_asterisks(password):
    """Display asterisks equal to the length of the password."""
    print("*" * len(password))


main()



