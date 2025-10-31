paragraph = '''This Python course is designed for beginners who want to learn Python programming. 
It covers basic syntax, data types, and introduces you to more advanced topics gradually.'''

length = len(paragraph)
first_char = paragraph[0]
last_char = paragraph[-1]
preview = paragraph[:50]
replaced_paragraph = paragraph.replace("Python", "PYTHON")
lowercase_paragraph = paragraph.lower()
trimmed_paragraph = paragraph.strip()
words = paragraph.split()

if "course" in paragraph:
    print("The word 'course' is found in the paragraph.")
final_message = "The course description is {} characters long and has {} words.".format(length, len(words))
print("Length:", length)
print("First character:", first_char)
print("Last character:", last_char)
print("Preview:", preview)
print("Replaced:", replaced_paragraph)
print("Lowercased:", lowercase_paragraph)
print("Trimmed:", trimmed_paragraph)
print("Words list:", words)
print(final_message)