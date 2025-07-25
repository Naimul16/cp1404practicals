"""
Programming Task - Instrument class
Time Planned: 30 mins
Time Taken: 45 mins
"""


class Instrument:
    """A simple representation of a musical instrument."""

    def __init__(self, model="", made_year=0, price=0):
        """Set up a new Instrument object."""
        self.model = model
        self.made_year = made_year
        self.price = price

    def calculate_age(self):
        """Return the age of the instrument from the year 2022."""
        reference_year = 2022  # Kept the same as original example
        return reference_year - self.made_year

    def is_classic(self):
        """Return True if the instrument is considered vintage (50+ years old)."""
        return self.calculate_age() >= 50

    def __str__(self):
        """Return a formatted string describing the instrument."""
        return f"{self.model} ({self.made_year}) : ${self.price:,.2f}"
