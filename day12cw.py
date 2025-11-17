try:
    title = input("Enter book title: ")
    year = input("Enter publication year: ")

    if not (title.replace(' ', '').isalpha()):
        raise ValueError("Title must contain only alphabets and spaces.")

    if not (year.isdigit() and len(year) == 4 and (year.startswith("19") or year.startswith("20"))):
        raise ValueError("Year must be a 4-digit number starting with 19 or 20.")

    print(f"Book accepted: '{title}' ({year})")
except Exception as e:
    print(f"Error: {e}")
finally:
    print("Library system input process completed.")
