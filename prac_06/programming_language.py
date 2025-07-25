"""
CP1404 Practical - CodingLanguage class
Time Estimated: 60 minutes
Time Taken: 90 minutes
"""


class CodingLanguage:
    """A simple model representing a coding language."""

    def __init__(self, language_name, type_system, supports_reflection, release_year):
        """Create a CodingLanguage instance."""
        self.language_name = language_name
        self.type_system = type_system
        self.supports_reflection = supports_reflection
        self.release_year = release_year

    def is_dynamically_typed(self):
        """Check if the language uses dynamic typing."""
        return self.type_system == "Dynamic"

    def __str__(self):
        """Return a readable description of the language."""
        return f"{self.language_name}, {self.type_system} Typing, Reflection={self.supports_reflection}, Introduced in {self.release_year}"
