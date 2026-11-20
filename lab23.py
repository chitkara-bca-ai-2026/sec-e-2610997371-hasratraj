# Lab 23 - File Handling Tool (student marks + class average)
import os

MARKS_FILE = "student_marks.txt"


def initialize_marks(filename):
    """Pre-populate the file with sample records (only if the file does not exist)."""
    if not os.path.exists(filename):
        with open(filename, "w") as file:
            file.write("Aman,85\n")
            file.write("Riya,92\n")
            file.write("Karan,78\n")


def store_student(filename, name, marks):
    """Append one 'Name,Marks' record to the file."""
    with open(filename, "a") as file:
        file.write(f"{name},{marks}\n")
    print(f"[SUCCESS] Record for '{name}' ({marks} marks) stored successfully.")


def display_and_calculate_average(filename):
    """Read all records, show a table and print total, count and class average."""
    if not os.path.exists(filename):
        print(f"[INFO] '{filename}' does not exist yet. Add some student marks first.")
        return

    names = []
    marks_list = []
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 2 and parts[1].strip().isdecimal():
                names.append(parts[0].strip())
                marks_list.append(int(parts[1]))

    if len(marks_list) == 0:
        print("[INFO] No student records found in the file.")
        return

    total_marks = sum(marks_list)
    avg = total_marks / len(marks_list)

    print(" STUDENT MARKS LEDGER ".center(52, "="))
    print(f"{'No.':<6}{'Student Name':<21}{'Marks Obtained'}")
    print("-" * 52)
    for number in range(len(marks_list)):
        print(f"{number + 1:<6}{names[number]:<21}{marks_list[number]}")
    print("=" * 52)
    print(f"{'Total Students':<15}: {len(marks_list)}")
    print(f"{'Total Marks':<15}: {total_marks}")
    print(f"{'Class Average':<15}: {avg:.2f}")
    print("=" * 52)


initialize_marks(MARKS_FILE)

print("=" * 45)
print("     STUDENT MARKS FILE HANDLING TOOL")
print("=" * 45)

# NOTE: the sample console output in the lab sheet shows
# 1 = Display Records & Class Average, 2 = Add & Store Student Marks.
while True:
    print("\nSelect an operation:")
    print("1. Display Records & Class Average")
    print("2. Add & Store Student Marks")
    print("3. Exit")

    choice = input("\nEnter choice (1-3): ").strip()

    if choice == "1":
        display_and_calculate_average(MARKS_FILE)

    elif choice == "2":
        name = input("Enter Student Name: ").strip()
        marks_text = input("Enter Marks (0-100): ").strip()

        if name == "" or "," in name:
            print("[ERROR] Name cannot be empty or contain a comma.")
        elif not marks_text.isdecimal() or int(marks_text) > 100:
            print("[ERROR] Invalid marks! Please enter a whole number between 0 and 100.")
        else:
            store_student(MARKS_FILE, name, int(marks_text))

    elif choice == "3":
        print("Thank you for using Student Marks Tool. Goodbye!")
        break

    else:
        print("[ERROR] Invalid choice! Please enter a number between 1 and 3.")