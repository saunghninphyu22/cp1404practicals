"""
Estimate: 30 minutes
Actual: 40 minutes
"""

from guitar import Guitar

FILENAME = "guitars.csv"

def main():
    """Read, display, add, and save guitars."""
    guitars = load_guitars(FILENAME)
    print("Guitars:")
    display_guitars(guitars)

    guitars.sort()
    print("\nSorted Guitars:")
    display_guitars(guitars)

    add_new_guitars(guitars)

    save_guitars(FILENAME, guitars)
    print(f"\nGuitars saved to {FILENAME}")


def load_guitars(filename):
    """Load guitars from CSV file."""
    guitars = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            name, year, cost = parts[0], int(parts[1]), float(parts[2])
            guitars.append(Guitar(name, year, cost))
    return guitars


def display_guitars(guitars):
    """Display list of guitars."""
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar}")


def add_new_guitars(guitars):
    """Prompt user to add new guitars."""
    print("\nAdd new guitars (leave name blank to stop):")
    name = input("Name: ").strip()
    while name:
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        name = input("Name: ").strip()


def save_guitars(filename, guitars):
    """Write guitars to CSV file."""
    with open(filename, 'w') as file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=file)


main()
