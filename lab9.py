# Lab 09 - Festival Decoration Designer
import sys


try:
    n = int(input("Enter the number of rows: "))
except ValueError:
    print("[ERROR] Please enter a valid whole number.")
    sys.exit()

if n <= 0:
    print("[ERROR] Number of rows must be greater than 0.")
    sys.exit()

DASH = "-" * 30


print("\nPattern 1: Star Triangle")
print(DASH)
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end=" " if j < i else "")
    print()


print("\nPattern 2: Number Triangle")
print(DASH)
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" " if j < i else "")
    print()


print("\nPattern 3: Inverted Star Triangle")
print(DASH)
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print("*", end=" " if j < i else "")
    print()


print("\nPattern 4: Pyramid")
print(DASH)
for i in range(1, n + 1):
    for _ in range(2 * (n - i)):          
        print(" ", end="")
    stars = 2 * i - 1
    for j in range(1, stars + 1):
        print("*", end=" " if j < stars else "")
    print()