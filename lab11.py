# Lab 11 - Online Account Registration


username = input("Enter your username: ")
password = input("Enter your password: ")


length_ok = len(password) >= 8
digit_ok = any(ch.isdigit() for ch in password)
upper_ok = any("A" <= ch <= "Z" for ch in password)

def status(passed):
    return "[PASS]" if passed else "[FAIL]"


LINE = "=" * 40
print(LINE)
print("PASSWORD VALIDATION REPORT")
print(LINE)
print(f"Username: {username}")
print(f"Password: {'*' * len(password)}")

print("\n--- Validation Rules ---")
print(f"{status(length_ok)} Minimum 8 characters ({len(password)} characters)")
print(f"{status(digit_ok)} At least one digit")
print(f"{status(upper_ok)} At least one uppercase letter")

print("\n--- Result ---")
if length_ok and digit_ok and upper_ok:
    print("Password is VALID!")
    print(f"Account created successfully for {username}!")
else:
    print("Password is INVALID")

print()
print(LINE)