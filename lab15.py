# Lab 15 - Student Information Management System (nested dictionaries)


students = {
    "101": {"Name": "Aman", "Branch": "BCA AI", "Semester": "1", "Marks": [85, 90, 78]},
    "102": {"Name": "Riya", "Branch": "BCA AI", "Semester": "1", "Marks": [92, 88, 95]},
    "103": {"Name": "Karan", "Branch": "BCA AI", "Semester": "1", "Marks": [74, 80, 82]},
}


def read_mark(subject_number):
    """Keep asking until a valid integer mark (0-100) is entered."""
    while True:
        text = input(f"  Subject {subject_number}: ").strip()
        try:
            mark = int(text)
        except ValueError:
            print("  [ERROR] Marks must be a whole number. Try again.")
            continue
        if 0 <= mark <= 100:
            return mark
        print("  [ERROR] Marks must be between 0 and 100. Try again.")


print("=" * 50)
print("     STUDENT INFORMATION MANAGEMENT SYSTEM")
print("=" * 50)

while True:
    print("\nSelect an operation:")
    print("1. View All Students")
    print("2. Search Student by Roll Number")
    print("3. Register New Student")
    print("4. Update Student Details")
    print("5. View Academic Performance")
    print("6. Delete Student Record")
    print("7. Exit")

    choice = input("\nEnter your choice (1-7): ").strip()

    if choice == "1":
        
        print("\n--- Enrolled Student Records ---")
        for roll, info in students.items():
            print(
                f"Roll No: {roll:<6}| Name: {info['Name']:<10} "
                f"| Branch: {info['Branch']} | Sem: {info['Semester']} "
                f"| Marks: {info['Marks']}"
            )
        print(f"Total Enrolled Students: {len(students)}")

    elif choice == "2":
        
        roll = input("Enter Roll Number to search: ").strip()
        student = students.get(roll)
        if student:
            print(f"\n[FOUND] Record for Roll No {roll}:")
            print(f"  Name     : {student['Name']}")
            print(f"  Branch   : {student['Branch']}")
            print(f"  Semester : {student['Semester']}")
            print(f"  Marks    : {student['Marks']}")
        else:
            print(f"\n[ERROR] No record found for Roll No {roll}.")

    elif choice == "3":
        
        print("\n--- Register New Student ---")
        roll = input("Enter Roll Number: ").strip()
        if roll == "":
            print("[ERROR] Roll Number cannot be empty.")
        elif roll in students:
            print(f"[ERROR] Roll Number {roll} already exists. Registration cancelled.")
        else:
            name = input("Enter Student Name: ").strip()
            branch = input("Enter Branch (e.g. BCA AI): ").strip()
            semester = input("Enter Semester: ").strip()
            print("Enter marks obtained in 3 subjects:")
            marks = [read_mark(i) for i in range(1, 4)]

            if name and branch and semester:
                students[roll] = {
                    "Name": name,
                    "Branch": branch,
                    "Semester": semester,
                    "Marks": marks,
                }
                print(f"\n[SUCCESS] Student '{name}' (Roll No: {roll}) registered successfully.")
            else:
                print("\n[ERROR] Name, Branch and Semester are required. Student not registered.")

    elif choice == "4":
        
        roll = input("Enter Roll Number to update: ").strip()
        student = students.get(roll)
        if student is None:
            print(f"[ERROR] No record found for Roll No {roll}.")
        else:
            print(f"Current details for {student['Name']} (Roll {roll}):")
            print(f"1. Branch: {student['Branch']} | 2. Semester: {student['Semester']}")
            field = input("Choose field to update (1 for Branch, 2 for Semester): ").strip()

            if field == "1":
                new_branch = input("Enter new branch: ").strip()
                if new_branch:
                    student["Branch"] = new_branch
                    print(f"[SUCCESS] Branch updated to '{new_branch}'.")
                else:
                    print("[ERROR] Branch cannot be empty.")
            elif field == "2":
                new_sem = input("Enter new semester: ").strip()
                if new_sem:
                    student["Semester"] = new_sem
                    print(f"[SUCCESS] Semester updated to '{new_sem}'.")
                else:
                    print("[ERROR] Semester cannot be empty.")
            else:
                print("[ERROR] Invalid field choice. Please choose 1 or 2.")

    elif choice == "5":
        
        roll = input("Enter Roll Number for Academic Performance: ").strip()
        student = students.get(roll)
        if student is None:
            print(f"\n[ERROR] No record found for Roll No {roll}.")
        else:
            total = sum(student["Marks"])
            average = total / len(student["Marks"])
            maximum = len(student["Marks"]) * 100
            result = "PASS" if average >= 40 else "FAIL"

            print("\n" + "=" * 16 + " ACADEMIC REPORT " + "=" * 16)
            print(f"Student Name : {student['Name']} (Roll: {roll})")
            print(f"Subject Marks: {student['Marks']}")
            print(f"Total Marks  : {total} / {maximum}")
            print(f"Average Marks: {average:.2f}%")
            print(f"Final Result : {result}")
            print("=" * 49)

    elif choice == "6":
        
        roll = input("Enter Roll Number to delete: ").strip()
        removed = students.pop(roll, None)
        if removed:
            print(f"\n[SUCCESS] Record for '{removed['Name']}' (Roll No: {roll}) deleted successfully.")
        else:
            print(f"\n[ERROR] No record found for Roll No {roll}.")

    elif choice == "7":
        
        print("\nThank you for using Student Information System.")
        print("Goodbye!")
        break

    else:
        print("\n[ERROR] Invalid choice! Please enter a number between 1 and 7.")