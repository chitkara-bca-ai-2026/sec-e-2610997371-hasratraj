# Lab 05 - Engineering Calculation Tool
import math

print("=" * 40)
print("      ENGINEERING CALCULATION TOOL")
print("=" * 40)


value = float(input("Enter a numerical value: "))


exponent = float(input("Enter an exponent: "))


decimal_value = float(input("Enter a decimal measurement: "))


power_result = math.pow(value, exponent)

if value >= 0:
    sqrt_text = f"{math.sqrt(value):.4f}"
else:
    sqrt_text = "Undefined (negative value)"

ceil_value = math.ceil(decimal_value)
floor_value = math.floor(decimal_value)


print("\n--- Results ---")
print(f"  {'Value':<18} : {value}")
print(f"  {'Exponent':<18} : {exponent}")
print(f"  {'Power (pow)':<18} : {power_result}")
print(f"  {'Square Root (sqrt)':<18} : {sqrt_text}")
print(f"  {'Decimal Value':<18} : {decimal_value}")
print(f"  {'Ceil Value':<18} : {ceil_value}")
print(f"  {'Floor Value':<18} : {floor_value}")
print("=" * 40)