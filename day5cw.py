python_students = {"Alice", "Bob", "Charlie"}
data_science_students = {"Bob", "David", "Eva"}

python_students.add("Frank")
data_science_students.remove("Eva")

both_courses = python_students.intersection(data_science_students)
only_python = python_students.difference(data_science_students)
all_students = python_students.union(data_science_students)

course_counts = {
    "Python": len(python_students),
    "Data Science": len(data_science_students)
}

for course, count in course_counts.items():
    print(f"Course: {course}, Students: {count}")

expected_growth = {course: count * 2 for course, count in course_counts.items()}

print("Students in both courses:", both_courses)
print("Students only in Python:", only_python)
print("All students in either course:", all_students)
print("Expected growth of students:", expected_growth)
