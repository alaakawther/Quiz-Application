from questions import questions

def run_quiz():
    score = 0

    for i, q in enumerate(questions):
        print()
        print(f"Question {i + 1}: {q['question']}")
        print(f"  1. {q['options'][0]}")
        print(f"  2. {q['options'][1]}")
        print(f"  3. {q['options'][2]}")

        answer = input("Your answer (1, 2 or 3): ")

        if answer == str(q['answer']):
            print("✓ Correct!")
            score += 1
        else:
            print(f"✗ Wrong! The correct answer was: {q['answer']}")

    print()
    print("========================")
    print(f"  Quiz finished!")
    print(f"  Your score: {score} / {len(questions)}")
    print("========================")