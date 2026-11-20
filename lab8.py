# Lab 08 - School Result Processing
import sys

LINE = "=" * 48
DASH = "-" * 48

print(LINE)
print("            SCHOOL RESULT PROCESSING")
print(LINE)


student_name = input("Enter Student Name : ")
roll_number = input("Enter Roll Number  : ")


print("\n--- Enter Marks for 5 Subjects (0-100) ---")
total_marks = 0.0
failed = False

for subject in range(1, 6):
    try:
        marks = float(input(f"Enter marks for Subject {subject}: "))
    except ValueError:
        print("\n[ERROR] Invalid input! Marks must be a number.")
        sys.exit()

    
    if marks < 0 or marks > 100:
        print("\n[ERROR] Invalid marks! Marks must be between 0 and 100.")
        sys.exit()

    
    if marks < 40:
        failed = True

    total_marks += marks


percentage = (total_marks / 500) * 100


if failed:
    result = "FAIL"
    grade = "F"
    remark = "Failed in one or more subjects"
else:
    result = "PASS"
    if percentage >= 90:
        grade, remark = "A+", "Outstanding"
    elif percentage >= 80:
        grade, remark = "A", "Excellent"
    elif percentage >= 70:
        grade, remark = "B", "Very Good"
    elif percentage >= 60:
        grade, remark = "C", "Good"
    elif percentage >= 50:
        grade, remark = "D", "Satisfactory"
    elif percentage >= 40:
        grade, remark = "E", "Pass"
    else:
        grade, remark = "F", "Fail"


print()
print(LINE)
print("                STUDENT REPORT CARD")
print(LINE)
print(f"  Student Name : {student_name}")
print(f"  Roll Number  : {roll_number}")
print(DASH)
print(f"  Total Marks  : {total_marks} / 500.0")
print(f"  Percentage   : {percentage:.2f}%")
print(f"  Result       : {result}")
print(f"  Grade        : {grade}")
print(f"  Remarks      : {remark}")
print(LINE)