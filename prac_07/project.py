"""Project class for project management program.

Estimated time: 1.5 hours
Actual time: 2 hours
"""

import datetime


import datetime


class Project:
    """Create a Project object"""

    def __init__(self, name, start_date, priority, estimate_cost, completion):
        """Initialize a Project instance: priority, completion, estimate_cost,
        import datetime to format the date"""
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = priority
        self.estimate_cost = estimate_cost
        self.completion = completion

    def __str__(self):
        """Return a string for name, start_date, priority, estimate_cost and completion"""
        return (
            f"{self.name}, start: {self.start_date.strftime("%d/%m/%Y")}, priority {self.priority},"
            f"estimate: ${self.estimate_cost:.2f}, completion: {self.completion}%")

    def is_complete(self):
        """Return True if completion is 100"""
        if self.completion == 100:
            return True

    def __lt__(self, other):
        """less than"""
        return self.priority < other.priority

    def is_updated_priority(self, new_priority):
        """Change priority to new_priority if the new priority is not empty"""
        if new_priority != "":
            self.priority = int(new_priority)

    def is_updated_completion(self, new_completion):
        """Change completion to new_completion if the new completion is not empty"""
        if new_completion != "":
            self.completion = int(new_completion)