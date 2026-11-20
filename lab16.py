# Lab 16 - Utility Calculator (Functions & Modular Programming)


import math


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return a minus b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return a / b, or None if b is zero (prevents a crash)."""
    if b == 0:
        return None
    return a / b


def modulus(a, b):
    """Return a % b, or None if b is zero (prevents a crash)."""
    if b == 0:
        return None
    return a % b


def power(base, exp=2):
    """Return base raised to exp. If exp is omitted, the base is squared."""
    return base ** exp


def format_number(n):
    """Return an int if n has no decimal part, otherwise return the float."""
    if n % 1 == 0:
        return int(n)
    return n



def is_number(text):
    """Check whether text looks like a valid decimal number."""
    text = text.strip()
    if text.startswith(("-", "+")):
        text = text[1:]
    if text.count(".") > 1:
        return False
    digits = text.replace(".", "")
    if digits == "":
        return False
    for ch in digits:
        if ch not in "0123456789":
            return False
    return True


def read_number(prompt):
    """Keep asking until the user enters a valid number, then return it as float."""
    while True:
        text = input(prompt).strip()
        if is_number(text):
            return float(text)
        print("[ERROR] Invalid number. Please enter a numeric value.")



history = []   


def run_operation(func, symbol):
    """Ask for two numbers, run func on them, show and record the result."""
    a = read_number("Enter first number: ")
    b = read_number("Enter second number: ")

    result = func(a, b)

    if result is None:
        if symbol == "/":
            print("[ERROR] Division by zero is not allowed.")
        else:
            print("[ERROR] Modulus by zero is not allowed.")
        return

    record = f"{format_number(a)} {symbol} {format_number(b)} = {format_number(result)}"
    history.append(record)
    print(f"[RESULT] {record}")


def run_power():
    """Handle the Power option, demonstrating the default argument exp=2."""
    base = read_number("Enter base number: ")
    exp_text = input("Enter exponent (press Enter for default 2): ").strip()

    if exp_text == "":
        exponent = 2
        result = power(base, exponent)
        print("[INFO] No exponent entered. Using default exponent: 2")
    else:
        if not is_number(exp_text):
            print("[ERROR] Invalid exponent. Please enter a numeric value.")
            return
        exponent = float(exp_text)

        
        if base == 0 and exponent < 0:
            print("[ERROR] Zero cannot be raised to a negative power.")
            return
        if base < 0 and exponent % 1 != 0:
            print("[ERROR] A negative base with a fractional exponent has no real result.")
            return
        if base != 0 and exponent * math.log10(abs(base)) > 300:
            print("[ERROR] Result is too large to calculate.")
            return

        result = power(base, exponent)

    record = f"{format_number(base)} ^ {format_number(exponent)} = {format_number(result)}"
    history.append(record)
    print(f"[RESULT] {record}")


def show_history():
    """Display the audit log of all calculations done in this session."""
    print("\n--- Calculation History ---")
    if len(history) == 0:
        print("[INFO] No calculations performed yet.")
    else:
        for number, record in enumerate(history, start=1):
            print(f"{number}. {record}")
        print(f"Total Calculations: {len(history)}")



print("=" * 50)
print("     ENTERPRISE MODULAR UTILITY CALCULATOR")
print("=" * 50)

while True:
    print("\nSelect an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus / Remainder (%)")
    print("6. Power / Exponentiation (Default: Square)")
    print("7. View Calculation History")
    print("8. Exit")

    choice = input("\nEnter your choice (1-8): ").strip()

    if choice == "1":
        run_operation(add, "+")
    elif choice == "2":
        run_operation(subtract, "-")
    elif choice == "3":
        run_operation(multiply, "*")
    elif choice == "4":
        run_operation(divide, "/")
    elif choice == "5":
        run_operation(modulus, "%")
    elif choice == "6":
        run_power()
    elif choice == "7":
        show_history()
    elif choice == "8":
        print("\nThank you for using the Enterprise Modular Utility Calculator. Goodbye!")
        break
    else:
        print("\n[ERROR] Invalid choice! Please enter a number between 1 and 8.")