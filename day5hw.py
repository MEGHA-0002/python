frontend_students = {"Alice", "Bob", "Carol"}
backend_students = {"Dave", "Bob", "Eve"}

backend_students.add("Frank")
frontend_students.remove("Carol")

both_courses = frontend_students.intersection(backend_students)
only_backend = backend_students.difference(frontend_students)
total_unique_students = frontend_students.union(backend_students)

course_counts = {
    "Frontend": len(frontend_students),
    "Backend": len(backend_students)
}

for course, count in course_counts.items():
    print(f"Course: {course}, Students: {count}")

# Method 1 (commented out): using dict() and then adding a new key
# combined_counts = dict(course_counts)
# combined_counts["Fullstack"] = len(total_unique_students)

combined_counts = {**course_counts, "Fullstack": len(total_unique_students)}

print("Students in both courses:", both_courses)
print("Students only in Backend:", only_backend)
print("Total unique students:", len(total_unique_students))
print("Combined course counts:", combined_counts)
