# Lab 14 - Library Book Collection (tuples and sets)


books = [
    ("Python Crash Course", "Eric Matthes", "2019", "Programming"),
    ("Automate the Boring Stuff", "Al Sweigart", "2020", "Programming"),
    ("Artificial Intelligence: A Modern Approach", "Stuart Russell", "2021", "AI"),
    ("Clean Code", "Robert C. Martin", "2008", "Software Engineering"),
]


library_categories = {book[3] for book in books}


student_wishlist = {"AI", "Cloud Computing", "Robotics", "Cybersecurity"}

print("=" * 50)
print("        LIBRARY BOOK & CATEGORY MANAGER")
print("=" * 50)

while True:
    print("\nSelect an operation:")
    print("1. View Cataloged Books")
    print("2. Add New Book Record")
    print("3. View Unique Library Categories")
    print("4. Add Category to Student Wishlist")
    print("5. Run Category Gap Analysis")
    print("6. Exit")

    choice = input("\nEnter your choice (1-6): ").strip()

    if choice == "1":
        
        print("\n--- Current Library Catalog (Fixed Records) ---")
        for count, (title, author, year, category) in enumerate(books, start=1):
            print(f'{count}. "{title}" by {author} ({year}) | Genre: {category}')
        print(f"Total Books: {len(books)}")

    elif choice == "2":
        
        print("\n--- Add New Book Record ---")
        title = input("Enter book title: ").strip()
        author = input("Enter author name: ").strip()
        year = input("Enter publication year: ").strip()
        category = input("Enter category/genre: ").strip()

        if title and author and year and category:
            new_book = (title, author, year, category)   
            books.append(new_book)
            library_categories.add(category)
            print(f'\n[SUCCESS] "{title}" added as an immutable catalog record.')
            print(f'[INFO] Category set updated with: "{category}"')
        else:
            print("\n[ERROR] All fields are required. Book was not added.")

    elif choice == "3":
        
        print("\n--- Unique Categories Available in Library (Set) ---")
        for category in sorted(library_categories):
            print(f"  - {category}")
        print(f"Total Unique Genres: {len(library_categories)}")

    elif choice == "4":
        
        print("\n--- Add to Student Wishlist ---")
        category = input("Enter requested category: ").strip()
        if category == "":
            print("[ERROR] Category cannot be empty.")
        elif category in student_wishlist:
            print(f'[INFO] "{category}" is already on the student wishlist.')
        else:
            student_wishlist.add(category)
            print(f'[SUCCESS] "{category}" added to student wishlist.')

    elif choice == "5":
        
        print("\n" + "=" * 16 + " CATEGORY GAP ANALYSIS " + "=" * 16)
        print(f"Library Holdings (Set):  {sorted(library_categories)}")
        print(f"Student Wishlist (Set):  {sorted(student_wishlist)}")
        print("-" * 55)

        in_stock = library_categories & student_wishlist
        to_purchase = student_wishlist - library_categories
        full_coverage = library_categories | student_wishlist

        print("1. Already in Stock (Intersection &):")
        print(f"   {sorted(in_stock)}")
        print("\n2. Purchase Order Needed (Difference -):")
        print(f"   {sorted(to_purchase)}")
        print("\n3. Full Combined Genre Coverage (Union |):")
        print(f"   {sorted(full_coverage)}")
        print("=" * 55)

    elif choice == "6":
        
        print("\nThank you for using the Library Manager. Goodbye!")
        break

    else:
        print("\n[ERROR] Invalid choice! Please enter a number between 1 and 6.")