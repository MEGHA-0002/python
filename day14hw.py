import random
import math


names_input = input("Enter names of customers who placed orders today (comma-separated): ")

names_list = [name.strip() for name in names_input.split(",") if name.strip()]
unique_names = list(set(names_list))

random.shuffle(unique_names)


total_unique = len(unique_names)
print(f"\nTotal number of unique participants: {total_unique}")

sqrt_unique = round(math.sqrt(total_unique))
print(f"Square root of participant count (rounded): {sqrt_unique}")


if total_unique >= 2:
    winners = random.sample(unique_names, 2)
else:
    winners = unique_names  
    
print("\nLucky Draw Winners (names reversed):")
for idx, winner in enumerate(winners, 1):
    print(f"Winner {idx}: {winner[::-1]}")
