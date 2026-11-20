# Lab 19 - Student Notes Management System (file write / read)
import os

NOTES_FILE = "notes.txt"


def write_notes(filename, content):
    """Write notes to the file in write mode ('w'), replacing any old content."""
    with open(filename, "w") as file:
        file.write(content)
    print(f"[SUCCESS] Notes successfully saved to '{filename}'.")


def read_notes(filename):
    """Return the notes text, or an info message if the file does not exist yet."""
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return file.read()
    return "[INFO] No notes file exists yet. Please write some notes first (option 1)."


print("=" * 45)
print("     STUDENT NOTES MANAGEMENT SYSTEM")
print("=" * 45)

while True:
    print("\nSelect an operation:")
    print("1. Write / Save Notes")
    print("2. View Saved Notes")
    print("3. Exit")

    choice = input("\nEnter choice (1-3): ").strip()

    if choice == "1":
        notes = input("Enter notes to save: ")
        if notes.strip() == "":
            print("[ERROR] Notes cannot be empty. Nothing was saved.")
        else:
            write_notes(NOTES_FILE, notes)

    elif choice == "2":
        print(f"--- Notes Content ({NOTES_FILE}) ---")
        print(read_notes(NOTES_FILE))

    elif choice == "3":
        print("Thank you for using the Notes Management System. Goodbye!")
        break

    else:
        print("[ERROR] Invalid choice! Please enter a number between 1 and 3.")