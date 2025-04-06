class Band:
    """Band class to represent a group of musicians."""

    def __init__(self, name=""):
        """Construct a Band with a name and an empty list of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return string representation of Band, including all musicians."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Make all musicians play and return the combined output."""
        return "\n".join(musician.play() for musician in self.musicians)
