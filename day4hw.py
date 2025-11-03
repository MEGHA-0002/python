web_dev = ["Rahul", "Priya", "Sonia"]
data_science = ["Meena", "Arjun", "Fatima"]
ui_ux = ["Vikas", "Sara", "Rekha"]

all_participants = [web_dev, data_science, ui_ux]

web_dev.append("Kiran")
data_science.insert(1, "Neeraj")
ui_ux.pop()

data_science_copy = data_science.copy()
data_science.clear()

print(web_dev[:2])
print([len(name) for name in data_science_copy])
print("Asha" in web_dev or "Asha" in data_science_copy or "Asha" in ui_ux)
print((web_dev[0], data_science_copy[0], ui_ux[0]))
