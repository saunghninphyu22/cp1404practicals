"""Main program for project management.

Estimated time: 2 hours
Actual time: 2.5 hours
"""

from project import Project
from operator import attrgetter
import datetime

FILENAME = "projects.txt"

MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""


def main():
    """Load projects from file and run program according to user choice"""
    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            user_file = input("Enter file name: ")
            projects = load_projects(user_file)
        elif choice == "S":
            save_projects(projects, FILENAME)
        elif choice == "D":
            completed_projects = []
            incomplete_projects = []
            for project in projects:
                if not project.is_complete():
                    incomplete_projects.append(project)
                else:
                    completed_projects.append(project)
            sort_projects(incomplete_projects, "Incomplete projects:")
            sort_projects(completed_projects, "Completed projects:")
        elif choice == "F":
            filter_projects(projects)
        elif choice == "A":
            add_projects(projects)
        elif choice == "U":
            for i in range(len(projects)):
                print(f"{i} {projects[i]}")
            update_projects(projects)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    saved_file = input(f"Would you like to save to {FILENAME}?: ").upper()
    if "Y" in saved_file:
        save_projects(projects, FILENAME)
    print("Thank you for using custom-built project management software.")


def update_projects(projects):
    """Update the new completion and new priority of the chosen project"""
    update_project_choice = validate_input_number("Project choice: ")
    while update_project_choice not in range(len(projects)):
        print("Invalid project choice")
        update_project_choice = validate_input_number("Project choice: ")
    print(projects[update_project_choice])
    new_completion = validate_new_number("New Percentage: ")
    new_priority = validate_new_number("New priority: ")
    projects[update_project_choice].is_updated_completion(new_completion)
    projects[update_project_choice].is_updated_priority(new_priority)


def sort_projects(texts, prompt):
    """Sort projects by priority"""
    texts.sort().__lt__(2)
    print(prompt)
    for text in texts:
        print(text)


def load_projects(filename):
    """Load projects from the file"""
    projects = []
    with open(filename, "r") as in_file:
        in_file.readline()
        for line in in_file:
            data = line.strip().split("\t")
            project = Project(data[0], data[1], int(data[2]), float(data[3]), int(data[4]))
            projects.append(project)
    return projects


def add_projects(projects):
    """Add a new project with new information to projects"""
    print("Let's add a new project")
    project_name = input("Name: ").title()
    while project_name == "":
        print("Input cannot be empty")
        project_name = input("Name: ").title()
    start_date = input("Start date (dd/mm/yy): ")
    while "/" not in start_date:
        print("Please write date in format (dd/mm/yy)")
        start_date = input("Start date (dd/mm/yy): ")
    priority = validate_input_number("Priority: ")
    estimate_cost = validate_input_number("Cost estimate: $")
    completed_percentage = validate_input_number("Percent complete: ")
    projects.append(Project(project_name, start_date, priority, estimate_cost, completed_percentage))
    return projects


def filter_projects(projects):
    """Filter projects by date"""
    filtered_date = input("Show projects that start after date (dd/mm/yy): ")
    filtered_date = datetime.datetime.strptime(filtered_date, "%d/%m/%Y").date()
    projects.sort(key=attrgetter("start_date"))
    for project in projects:
        if project.start_date >= filtered_date:
            print(project)


def validate_input_number(prompt):
    """Validate user input number"""
    valid_input = False
    while not valid_input:
        try:
            number = int(input(prompt))
            valid_input = True
            return number
        except ValueError:
            print("Invalid input")


def validate_new_number(prompt):
    """Validate new user input"""
    new_number = input(prompt)
    if new_number != "":
        while not new_number.isdigit():
            print("Invalid input")
            new_number = input(prompt)
    else:
        new_number = ""
    return new_number


def save_projects(projects, filename):
    """Save projects to the file"""
    with open(filename, "w") as out_file:
        out_file.write("Name	Start Date	Priority	Cost Estimate	Completion Percentage\n")
        for project in projects:
            out_file.write(f"{project.name}\t{project.start_date.strftime("%d/%m/%Y")}\t{project.priority}"
                           f"\t{project.estimate_cost:.2f}\t{project.completion}\n")


main()
