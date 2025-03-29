"""
Estimate: 10 minutes
Actual: 12 minutes
"""

class ProgrammingLanguage:
    """ A Programming Language class with a name, type, reflection and year."""
    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Check if the programming language is dynamic."""
        return self.typing.lower() == "dynamic"

    def __str__(self):
        """Return a string representation of the programming language."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"