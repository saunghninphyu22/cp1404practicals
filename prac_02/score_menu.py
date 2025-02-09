"""
Score menu program with functions for validation, result determination, and star display.
"""

MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    """Main function to handle menu operations."""
    score = get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(f"Result: {determine_score_result(score)}")
        elif choice == "S":
            print(show_stars(score))
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()

    print("Goodbye!")


def get_valid_score():
    """Prompt user for a valid score between 0 and 100."""
    score = int(input("Enter score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score. Please enter a score between 0 and 100.")
        score = int(input("Enter score (0-100): "))
    return score


def determine_score_result(score):
    """Determine the result for a given score."""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Pass"
    else:
        return "Bad"


def show_stars(score):
    """Return a string of stars equal to the score."""
    return "*" * score


main()
