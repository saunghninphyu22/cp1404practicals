"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
        A ValueError occurs when the user enters a text instead of a number.
2. When will a ZeroDivisionError occur?
        A ZeroDivisionError occurs when the user enters 0 for the denominator.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("The denominator cannot be zero")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")