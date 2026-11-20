# Lab 13 - Inventory Control System

inventory = ["Notebook", "Pen", "Eraser", "Ruler"]

print("=" * 44)
print("        INVENTORY CONTROL SYSTEM")
print("=" * 44)

while True:
    print("\nSelect an operation:")
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Sort Inventory")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ").strip()

    if choice == "1":
        
        print("\n--- Current Inventory ---")
        if len(inventory) == 0:
            print("Inventory is empty.")
        else:
            for number, item in enumerate(inventory, start=1):
                print(f"{number}. {item}")

    elif choice == "2":
        
        item = input("Enter item name to add: ").strip()
        if item == "":
            print("[ERROR] Item name cannot be empty.")
        else:
            inventory.append(item)
            print(f'[SUCCESS] "{item}" added to inventory.')

    elif choice == "3":
        
        item = input("Enter item name to remove: ").strip()
        if item in inventory:
            inventory.remove(item)
            print(f'[SUCCESS] "{item}" removed from inventory.')
        else:
            print(f'[ERROR] "{item}" not found in inventory.')

    elif choice == "4":
        
        inventory.sort(key=str.lower)
        print("\n[SUCCESS] Inventory sorted alphabetically.")
        print("Updated Inventory:")
        for number, item in enumerate(inventory, start=1):
            print(f"{number}. {item}")

    elif choice == "5":
        
        print("\nThank you for using the Inventory Control System. Goodbye!")
        break

    else:
        print("\n[ERROR] Invalid choice! Please enter a number between 1 and 5.")