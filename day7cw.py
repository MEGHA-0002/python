grocery_list = ["milk", "bread", "eggs"]

def add_item(item):
    grocery_list.append(item)
    return grocery_list

def remove_last_item():
    grocery_list.pop()
    return grocery_list

display_list = lambda items: [print(f"items : {item}") for item in items]

def count_characters(items):
    if not items:  
        return 0
    return len(items[0]) + count_characters(items[1:])

print(add_item("butter"))
print(remove_last_item())
display_list(grocery_list)
print(count_characters(grocery_list))
