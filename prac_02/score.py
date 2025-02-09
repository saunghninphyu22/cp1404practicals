"""
CP1404/CP5632 - Practical
Program to determine score status with proper functions.
"""

import random


def main():
    """Main function to get user score and display results."""
    score = float(input("Enter score: "))
    result = determine_score_status(score)
    print(result)

    # Generate a random score and display the result
    random_score = random.randint(0, 100)
    print(f"Random score: {random_score:.2f} - {determine_score_status(random_score)}")


def determine_score_status(score):
    """
    Determine the status of a score.
    """
    if score < 0 or score > 100:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Pass"
    else:
        return "Excellent"


main()
