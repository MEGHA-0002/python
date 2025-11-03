fruits = ["Apple", "Banana", "Mango"]
vegetables = ["Carrot", "Potato", "Beans"]
beverages = ["Juice", "Milk", "Water"]

fruits.append("Orange")
vegetables.insert(1, "Tomato")
beverages.pop()

inventory = [fruits, vegetables, beverages]

print(fruits[:2])
print(vegetables[-1])
print([len(item) for item in fruits])
print("Water" in beverages)
print((fruits[0], vegetables[0], beverages[0]))
