"""
CP1404/CP5632 Practical
Reading subject data from a file into a list
"""

DATA_FILE = "subject_data.txt"


def main():
    subject_list = read_subject_file()
    show_subject_info(subject_list)


def read_subject_file():
    """Load subject information from file. Format: subject,lecturer,student_count"""
    file = open(DATA_FILE, 'r')
    data_entries = []
    for entry in file:
        entry = entry.strip()  # Clean up line breaks
        info = entry.split(',')  # Separate each part
        info[2] = int(info[2])  # Convert number of students to integer
        data_entries.append(info)
    file.close()
    return data_entries


def show_subject_info(data_entries):
    """Display each subject’s details in a readable format."""
    for subject_code, teacher, student_total in data_entries:
        print(f"{subject_code} is taught by {teacher} and has {student_total} students.")


main()
