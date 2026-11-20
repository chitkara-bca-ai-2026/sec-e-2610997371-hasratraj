# Lab 18 - Mathematics Learning Tool (recursion)


def factorial(n):
    """Return n! using recursion."""
    if n <= 1:                      # base case
        return 1
    return n * factorial(n - 1)     # recursive step


def fibonacci(n):
    """Return the n-th Fibonacci number (0-indexed) using recursion."""
    if n == 0:                      # base cases
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)   # recursive step


print("=" * 45)
print("       MATHEMATICS LEARNING TOOL")
print("=" * 45)

while True:
    print("\nSelect an operation:")
    print("1. Calculate Factorial")
    print("2. Generate Fibonacci Series")
    print("3. Exit")

    choice = input("\nEnter choice (1-3): ").strip()

    if choice == "1":
        text = input("Enter a non-negative integer: ").strip()
        if not text.isdecimal():
            print("[ERROR] Please enter a non-negative whole number (n >= 0).")
        elif int(text) > 500:
            print("[ERROR] Please enter a number up to 500 (recursion depth limit).")
        else:
            n = int(text)
            print(f"[RESULT] Factorial of {n} ({n}!) = {factorial(n)}")

    elif choice == "2":
        text = input("Enter number of terms to generate: ").strip()
        if not text.isdecimal() or int(text) < 1:
            print("[ERROR] Please enter a positive whole number of terms.")
        elif int(text) > 30:
            print("[ERROR] Please enter at most 30 terms (recursive Fibonacci gets very slow after that).")
        else:
            terms = int(text)
            series = []
            for i in range(terms):
                series.append(fibonacci(i))
            print(f"[RESULT] Fibonacci series ({terms} terms): {series}")

    elif choice == "3":
        print("Thank you for using the Mathematics Learning Tool. Goodbye!")
        break

    else:
        print("[ERROR] Invalid choice! Please enter a number between 1 and 3.")