"""
Estimate: 10 minutes
Actual: 15 minutes
"""

CURRENT_YEAR = 2025

class Guitar:
    """A guitar class with a name, year, and cost."""

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a formatted string representation of the Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def get_age(self):
        """Return the age of the Guitar."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Return True if the guitar is 50 or more years old, False otherwise."""
        return self.get_age() >= 50

    def __lt__(self, other):
        """Compare guitars by year (older first)."""
        return self.year < other.year
