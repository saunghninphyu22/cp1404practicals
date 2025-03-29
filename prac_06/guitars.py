"""
Estimate: 30 minutes
Actual: 35 minutes
"""

from guitar import Guitar

def main():
    """Allow user to enter guitar and display their details."""
    guitars = []
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added.\n")
        name = input("Name: ")
    print("\n... snip ...\n")
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        name_width = max((len(guitar.name) for guitar in guitars))
        cost_width = max((len(f"{guitar.cost:.2f}") for guitar in guitars))
        print(
            f"Guitar {i}: {guitar.name:>{name_width}} ({guitar.year}), worth $ {guitar.cost:{cost_width}.2f}{vintage_string}")

main()