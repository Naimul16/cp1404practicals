"""
Project class for the Project Management Program.
Estimate: 50 minutes
Actual: 70 min+
"""

import datetime

class Project:
    """Represent a project."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = start_date  # should be a datetime.date object
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __lt__(self, other):
        """Define ordering of Projects based on priority value."""
        return self.priority < other.priority

    def is_complete(self):
        """Determine if a project is fully completed (100%)."""
        return self.completion_percentage == 100

    def __str__(self):
        """Return a nicely formatted string of the project's details."""
        date_str = self.start_date.strftime("%d/%m/%Y")
        return (f"{self.name}, start: {date_str}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%")

    @staticmethod
    def from_line(line):
        """Construct a Project object from a tab-separated data line."""
        parts = line.strip().split('\t')
        name = parts[0]
        start_date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
        priority = int(parts[2])
        cost_estimate = float(parts[3])
        completion_percentage = int(parts[4])
        return Project(name, start_date, priority, cost_estimate, completion_percentage)

    def to_line(self):
        """Convert the Project object into a tab-separated string for saving."""
        date_str = self.start_date.strftime("%d/%m/%Y")
        return f"{self.name}\t{date_str}\t{self.priority}\t{self.cost_estimate}\t{self.completion_percentage}"
