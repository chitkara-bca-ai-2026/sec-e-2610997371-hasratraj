# Lab 04 - Data Conversion Utility

LINE = "=" * 50
DASH = "-" * 50

print(LINE)
print("              DATA CONVERSION UTILITY")
print(LINE)


product_name = input("Enter Product Name : ")
price = float(input("Enter Price        : "))
quantity = int(input("Enter Quantity     : "))


total_price = price * quantity


amount_str = str(total_price)


print()
print(DASH)
print("              TYPE CASTING SUMMARY")
print(DASH)
print(f"{'Variable':<17}{'Value':<17}{'Python Type'}")
print(DASH)
print(f"{'product_name':<17}{product_name:<17}{type(product_name)}")
print(f"{'price':<17}{price:<17}{type(price)}")
print(f"{'quantity':<17}{quantity:<17}{type(quantity)}")
print(f"{'total_price':<17}{total_price:<17}{type(total_price)}")
print(f"{'amount_str':<17}{amount_str:<17}{type(amount_str)}")
print(DASH)


print("\n")
print(DASH)
print("                    TAX INVOICE")
print(DASH)
print(f"  Product Name   : {product_name}")
print(f"  Price per Unit : Rs. {price:.2f}")
print(f"  Quantity       : {quantity}")
print("  " + "-" * 40)
print(f"  Invoice Total  : Rs. {amount_str}")
print(LINE)