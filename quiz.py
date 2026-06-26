import random
from questions import questions
from scores import save_score
from utils import get_valid_answer    
def run_quiz(player_name):
    score = 0

    shuffled_questions = questions.copy()
    random.shuffle(shuffled_questions)

    print(f"\nGood luck, {player_name}! Here we go...\n")

    for i, q in enumerate(shuffled_questions):
        print()
        print(f"Question {i + 1}: {q['question']}")
        print(f"  1. {q['options'][0]}")
        print(f"  2. {q['options'][1]}")
        print(f"  3. {q['options'][2]}")

        answer = get_valid_answer(3)

        if answer == str(q['answer']):
            print("✓ Correct!")
            score += 1
        else:
            correct_text = q['options'][q['answer'] - 1]
            print("✗ Wrong!")
            print(f"  Correct answer: {correct_text}")

    total = len(shuffled_questions)

    print()
    print("========================")
    print("  Quiz finished!")
    print(f"  Your score: {score} / {total}")
    print("========================")

    save_score(player_name, score, total)

    return score, total