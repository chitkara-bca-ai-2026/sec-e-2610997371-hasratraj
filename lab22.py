# Lab 22 - Keyword Search Utility
import os

REPORT_FILE = "report.txt"


def initialize_report(filename):
    """Pre-populate the report with sample text (only if the file does not exist)."""
    if not os.path.exists(filename):
        with open(filename, "w") as file:
            file.write("Annual Technology and AI Progress Report.\n")
            file.write("The adoption of Artificial Intelligence accelerated across business units.\n")
            file.write("AI algorithms improved diagnostic accuracy in healthcare operations.\n")
            file.write("Data engineering pipelines were upgraded to support real-time data streaming.\n")
            file.write("The company plans further investments in AI research and machine learning.\n")


def search_keyword(filename, keyword):
    """Case-insensitive search; show matching lines, line numbers and total count."""
    if not os.path.exists(filename):
        print(f"[ERROR] File '{filename}' not found.")
        return

    total = 0
    print(f"--- Search Results for '{keyword}' ---")
    with open(filename, "r") as file:
        for line_number, line in enumerate(file, start=1):
            if keyword.lower() in line.lower():
                count = line.lower().count(keyword.lower())
                total += count
                label = "match" if count == 1 else "matches"
                print(f"Line {line_number:>2} ({count} {label}): {line.rstrip()}")

    if total > 0:
        print(f"\n[FOUND] Total occurrences of '{keyword}': {total}")
    else:
        print(f"\n[NOT FOUND] '{keyword}' does not appear in the document.")


def display_document(filename):
    """Read and display all lines of the document with line numbers."""
    if not os.path.exists(filename):
        print(f"[ERROR] File '{filename}' not found.")
        return

    print(f"--- Full Report Document ({filename}) ---")
    with open(filename, "r") as file:
        for line_number, line in enumerate(file, start=1):
            print(f"{line_number:>2} | {line.rstrip()}")


initialize_report(REPORT_FILE)

print("=" * 45)
print("          KEYWORD SEARCH UTILITY")
print("=" * 45)

while True:
    print("\nSelect an operation:")
    print("1. Search Keyword in Document")
    print("2. View Full Document")
    print("3. Exit")

    choice = input("\nEnter choice (1-3): ").strip()

    if choice == "1":
        keyword = input("Enter keyword to search: ").strip()
        if keyword == "":
            print("[ERROR] Keyword cannot be empty.")
        else:
            search_keyword(REPORT_FILE, keyword)

    elif choice == "2":
        display_document(REPORT_FILE)

    elif choice == "3":
        print("Thank you for using Keyword Search Utility. Goodbye!")
        break

    else:
        print("[ERROR] Invalid choice! Please enter a number between 1 and 3.")