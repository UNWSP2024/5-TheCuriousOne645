import random

def generate_question():
    """Generate a random addition question."""
    num1 = random.randint(1, 999)
    num2 = random.randint(1, 999)
    return num1, num2

def check_answer(num1, num2, student_answer):
    """Check if the student's answer is correct."""
    correct_answer = num1 + num2
    return student_answer == correct_answer, correct_answer

def main():
    """Main function to run the math quiz."""
    num1, num2 = generate_question()
    print(f"\n {num1}\n+{num2}\n------")
    
    try:
        student_answer = int(input("Enter your answer: "))
        is_correct, correct_answer = check_answer(num1, num2, student_answer)
        
        if is_correct:
            print("Congratulations! Your answer is correct.")
        else:
            print(f"Oops! The correct answer is {correct_answer}.")
    except ValueError:
        print("Please enter a valid number.")
    
if __name__ == "__main__":
    main()
