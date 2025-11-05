attendance = [18, 20, 19, 15, 21]

full_days_count = 0
for day_attendance in attendance:
    if day_attendance >= 20:
        print("Full")
        full_days_count += 1
    else:
        print("Not Full")

total_attendance = sum(attendance)

print("Number of full days:", full_days_count)
print("Total attendance:", total_attendance)
