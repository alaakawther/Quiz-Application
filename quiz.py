import random
from questions import questions
from utils import get_valid_answer


def run_quiz(player_name):
    shuffled_questions = questions.copy()
    random.shuffle(shuffled_questions)

    score = 0
    total = len(shuffled_questions)

    print(f"\n{'='*55}")
    print(f"  Welcome, {player_name}! The quiz is starting...")
    print(f"  Answer each question by typing 1, 2, or 3.")
    print(f"{'='*55}\n")

    for index, q in enumerate(shuffled_questions, start=1):
        print(f"Question {index}/{total}:")
        print(f"  {q['question']}\n")

        for i, option in enumerate(q["options"], start=1):
            label = chr(64 + i)
            print(f"  {i}) {label}) {option}")

        print()
        answer = get_valid_answer(len(q["options"]))

        if answer == str(q["answer"]):
            print("✅  Correct!\n")
            score += 1
        else:
            correct_label = chr(64 + q["answer"])
            correct_text = q["options"][q["answer"] - 1]
            print(f"❌  Wrong! The correct answer was {correct_label}) {correct_text}\n")

        print("-" * 55)

    print(f"\n{'='*55}")
    print(f"  Quiz finished! You scored {score} out of {total}.")

    percentage = (score / total) * 100
    if percentage == 100:
        print(" Perfect score! Outstanding!")
    elif percentage >= 80:
        print(" Great job!")
    elif percentage >= 50:
        print(" Good effort — keep practising!")
    else:
        print("  Keep studying — you'll get there!")

    print(f"{'='*55}\n")

    return score, total