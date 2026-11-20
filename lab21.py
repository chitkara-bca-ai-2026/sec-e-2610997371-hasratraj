# Lab 21 - Document Statistics Tool (lines, words, characters)
import os

DOC_FILE = "document.txt"


def initialize_document(filename):
    """Pre-populate the document with sample text (only if the file does not exist)."""
    if not os.path.exists(filename):
        with open(filename, "w") as file:
            file.write("Artificial Intelligence is transforming modern industries.\n")
            file.write("Python provides powerful libraries for text processing and data analysis.\n")
            file.write("Developers use file handling to store and retrieve persistent records.\n")
            file.write("Modular programming ensures code is clean, reusable, and easy to maintain.\n")


def get_document_statistics(filename):
    """Return (line_count, word_count, char_count), or None if the file is missing."""
    if not os.path.exists(filename):
        return None

    with open(filename, "r") as file:
        lines = file.readlines()

    line_count = len(lines)
    word_count = 0
    char_count = 0
    for line in lines:
        word_count += len(line.split())
        char_count += len(line)
    return (line_count, word_count, char_count)


def display_document(filename):
    """Print each line prefixed by its line number."""
    if not os.path.exists(filename):
        print(f"[ERROR] File '{filename}' not found.")
        return

    print(f"--- Document Preview ({filename}) ---")
    with open(filename, "r") as file:
        for number, line in enumerate(file, start=1):
            print(f"{number:>3} | {line.rstrip()}")


initialize_document(DOC_FILE)

print("=" * 45)
print("        DOCUMENT STATISTICS ANALYZER")
print("=" * 45)

while True:
    print("\nSelect an operation:")
    print("1. Calculate Document Statistics")
    print("2. Display Document Content")
    print("3. Exit")

    choice = input("\nEnter choice (1-3): ").strip()

    if choice == "1":
        stats = get_document_statistics(DOC_FILE)
        if stats is None:
            print(f"[ERROR] File '{DOC_FILE}' not found.")
        else:
            lines, words, chars = stats
            print(" DOCUMENT REPORT ".center(49, "="))
            print(f"{'Target File':<17}: {DOC_FILE}")
            print(f"{'Total Lines':<17}: {lines}")
            print(f"{'Total Words':<17}: {words}")
            print(f"{'Total Characters':<17}: {chars}")
            print()
            print("=" * 49)

    elif choice == "2":
        display_document(DOC_FILE)

    elif choice == "3":
        print("Thank you for using Document Statistics Analyzer. Goodbye!")
        break

    else:
        print("[ERROR] Invalid choice! Please enter a number between 1 and 3.")