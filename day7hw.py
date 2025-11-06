inventory = []

def add_item(item):
    inventory.append(item)
    return inventory

def count_items(items):
    if not items:
        return 0
    return 1 + count_items(items[1:])

show_item = lambda item: print(f"Item in Stock: {item}")

def main():
    add_item("dog food")
    add_item("cat toy")
    add_item("bird cage")
    add_item("fish tank")

    for item in inventory:
        show_item(item)

    print("Total items in stock:", count_items(inventory))

main()
