item = input("Enter the name of a new item: ")


with open("items.txt", "a") as file:
    file.write(item + "\n")

print("\nCurrent list of items:")
with open("items.txt", "r") as file:
    items = file.readlines()
    for item in items:
        print(item.strip())
