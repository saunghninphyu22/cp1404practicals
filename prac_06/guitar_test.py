"""
Estimate: 15 minutes
Actual: 20 minutes
"""
from guitar import Guitar

def main():
    """Test get_age() and is_vintage() methods of Guitar class."""
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 500)
    print(f"{gibson.name} get_age() - Expected 103. Got {gibson.get_age()}")
    print(f"{another_guitar.name} get_age() - Expected 12. Got {another_guitar.get_age()}")
    print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage()}")
    print(f"{another_guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage()}")

main()

