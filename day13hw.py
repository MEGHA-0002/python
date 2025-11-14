filename = "students.txt"

try:
    with open(filename, "r") as file:
        print("Existing student names:")
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("No existing student names found.")

count = int(input("How many student names do you want to add? "))


with open(filename, "a") as file:
    for i in range(count):
        name = input(f"Enter name of student {i + 1}: ")
        file.write(name + "\n")


print("\nUpdated student list:")
with open(filename, "r") as file:
    for line in file:
        print(line.strip())
