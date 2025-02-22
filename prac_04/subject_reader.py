"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    display_subject_details(data)


def display_subject_details(data):
    """Display each subject's details."""
    lecturer_width = max(len(parts[1]) for parts in data)
    number_of_students_width = max(len(str(parts[2])) for parts in data)
    for data in data:
        subject, lecturer, number_of_students = data
        print(f"{subject} is taught by {lecturer:{lecturer_width}} and has {number_of_students:{number_of_students_width}} students")


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    with open(FILENAME) as input_file:
        for line in input_file:
            line = line.strip()
            parts = line.split(',')
            parts[2] = int(parts[2])
            data.append(parts)
    return data
main()