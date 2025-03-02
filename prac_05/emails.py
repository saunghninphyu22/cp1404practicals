"""
Emails
Estimate: 40 minutes
Actual:  37  minutes
"""


def main():
    """Print user's name and email"""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        username = obtain_name_from_email(email)
        name = confirm_name(username)
        email_to_name[email] = name
        email = input("Email: ")
    for email, username in email_to_name.items():
        print(f"{username} ({email})")


def confirm_name(username):
    """Confirm and get the user's name"""
    enquiry = input(f"Is your name {username}? (Y/n) ").lower()
    if enquiry != "y" and enquiry != "":
        username = input("Name: ")
    return username


def obtain_name_from_email(email):
    """Obtain name from email"""
    string = email.split("@")[0]
    name = string.split(".")
    return " ".join(name).title()


main()