# Lab 07 - Calendar Verification System
import sys

print("=" * 40)
print("     CALENDAR VERIFICATION SYSTEM")
print("=" * 40)


try:
    year = int(input("Enter year: "))
except ValueError:
    print("\n[ERROR] Invalid input! Please enter a whole number for the year.")
    sys.exit()


if year <= 0:
    print("\n[ERROR] Year must be a positive integer greater than 0.")
    sys.exit()


if year % 100 == 0:                      
    if year % 400 == 0:
        is_leap = True
        reason = "Century year divisible by 400"
    else:
        is_leap = False
        reason = "Century year not divisible by 400"
else:                                    
    if year % 4 == 0:
        is_leap = True
        reason = "Divisible by 4 and not a century year"
    else:
        is_leap = False
        reason = "Not divisible by 4"


if is_leap:
    status = "LEAP YEAR"
    days_in_year = 366
    days_in_february = 29
else:
    status = "COMMON YEAR"
    days_in_year = 365
    days_in_february = 28


print()
print("-" * 40)
print(f"Year: {year}")
print(f"Status: {status}")
print(f"Days in Year: {days_in_year} days")
print(f"Days in February: {days_in_february} days")
print(f"Reason: {reason}")
print("-" * 40)