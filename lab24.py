# Lab 24 - Student Result Analysis System (CSV handling)
import csv
import os

CSV_FILE = "students_data.csv"


def initialize_csv(filename):
    """Pre-populate the CSV with sample records (only if the file does not exist)."""
    if not os.path.exists(filename):
        records = [
            ["101", "Aman", "Python", "85"],
            ["102", "Riya", "Python", "92"],
            ["103", "Karan", "Python", "45"],
            ["104", "Neha", "Python", "78"],
            ["105", "Rohit", "Python", "38"],
            ["106", "Pooja", "Python", "62"],
        ]
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["RollNo", "Name", "Subject", "Marks"])
            writer.writerows(records)


def print_table(rows):
    """Print rows (dicts) in a structured tabular format."""
    print(f"{'Roll No':<11}{'Name':<16}{'Subject':<13}{'Marks'}")
    print("-" * 48)
    for row in rows:
        print(f"{row['RollNo']:<11}{row['Name']:<16}{row['Subject']:<13}{row['Marks']}")
    print("=" * 48)


def read_all_students(filename):
    """Read the CSV file and print all rows in a table."""
    if not os.path.exists(filename):
        print(f"[ERROR] File '{filename}' not found.")
        return

    with open(filename, "r", newline="") as file:
        rows = list(csv.DictReader(file))

    print(" ALL ENROLLED STUDENTS ".center(48, "="))
    print_table(rows)
    print(f"Total Records: {len(rows)}")


def filter_students_above_threshold(filename, threshold=50):
    """Show only the students whose marks are strictly greater than threshold."""
    if not os.path.exists(filename):
        print(f"[ERROR] File '{filename}' not found.")
        return

    qualified = []
    with open(filename, "r", newline="") as file:
        for row in csv.DictReader(file):
            marks_text = row["Marks"].strip()
            if marks_text.isdecimal() and int(marks_text) > threshold:
                qualified.append(row)

    print(f" STUDENTS WITH MARKS > {threshold} ".center(48, "="))
    print_table(qualified)
    print(f"Qualified Students Count: {len(qualified)}")


initialize_csv(CSV_FILE)

print("=" * 45)
print("      STUDENT RESULT ANALYSIS SYSTEM")
print("=" * 45)

while True:
    print("\nSelect an operation:")
    print("1. Display All Students from CSV")
    print("2. Filter Students (Marks > 50)")
    print("3. Exit")

    choice = input("\nEnter choice (1-3): ").strip()

    if choice == "1":
        read_all_students(CSV_FILE)

    elif choice == "2":
        filter_students_above_threshold(CSV_FILE, 50)

    elif choice == "3":
        print("Thank you for using Student Result Analysis System. Goodbye!")
        break

    else:
        print("[ERROR] Invalid choice! Please enter a number between 1 and 3.")
