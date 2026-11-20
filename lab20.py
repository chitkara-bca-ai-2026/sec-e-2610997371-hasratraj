# Lab 20 - Daily Log Book (file appending)
import os
from datetime import datetime

LOG_FILE = "daily_log.txt"


def initialize_log(filename):
    """Pre-populate the log with sample entries (only if the file does not exist)."""
    if not os.path.exists(filename):
        with open(filename, "w") as file:
            file.write("09:00 AM - System server startup verified.\n")
            file.write("10:30 AM - Morning attendance synchronized.\n")


def append_entry(filename, entry):
    """Append one entry on a new line without touching earlier entries."""
    with open(filename, "a") as file:
        file.write(entry + "\n")
    print(f"[SUCCESS] New entry logged to '{filename}'.")


def display_log(filename):
    """Read the log file and display all entries with a count."""
    if not os.path.exists(filename):
        print(f"[INFO] '{filename}' does not exist yet. Add a log entry first.")
        return

    with open(filename, "r") as file:
        entries = [line.rstrip("\n") for line in file if line.strip() != ""]

    print(" DAILY LOG BOOK ".center(48, "="))
    for number, entry in enumerate(entries, start=1):
        print(f"[{number:02d}] {entry}")
    print(f"\nTotal Logged Entries: {len(entries)}")
    print("=" * 48)


initialize_log(LOG_FILE)

print("=" * 45)
print("            OFFICE DAILY LOG BOOK")
print("=" * 45)

while True:
    print("\nSelect an operation:")
    print("1. Add Log Entry")
    print("2. Display Complete Log")
    print("3. Exit")

    choice = input("\nEnter choice (1-3): ").strip()

    if choice == "1":
        message = input("Enter log entry: ").strip()
        if message == "":
            print("[ERROR] Log entry cannot be empty.")
        else:
            timestamp = datetime.now().strftime("%I:%M %p")
            append_entry(LOG_FILE, f"{timestamp} - {message}")

    elif choice == "2":
        display_log(LOG_FILE)

    elif choice == "3":
        print("Thank you for using the Daily Log Book. Goodbye!")
        break

    else:
        print("[ERROR] Invalid choice! Please enter a number between 1 and 3.")