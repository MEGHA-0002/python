import random
import math

names_input = input("Enter the names of invited guests (comma-separated): ")


names_list = [name.strip() for name in names_input.split(",") if name.strip()]
unique_names = list(set(names_list))


total_unique = len(unique_names)
print(f"\nTotal number of unique names: {total_unique}")


sqrt_unique = round(math.sqrt(total_unique))
print(f"Rounded square root of the total: {sqrt_unique}")


selected_name = random.choice(unique_names)
print(f"\nSelected name for the game: {selected_name}")


reversed_name = selected_name[::-1]
print(f"Reversed selected name: {reversed_name}")
