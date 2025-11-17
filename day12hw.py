try:
    name = input("Enter your name: ")
    feedback = input("Enter your feedback: ")

    if not name.strip() or not feedback.strip():
        raise ValueError("Name and feedback cannot be empty.")

    print(f"Thank you, {name}! Your feedback: \"{feedback}\" has been recorded.")
except Exception as e:
    print(f"Error: {e}")
finally:
    print("Feedback process completed.")
