from quiz import run_quiz
from scores import save_score, show_scores


def get_player_name():
    while True:
        name = input("Enter your name: ").strip()
        if name:
            return name
        print("⚠  Name cannot be empty. Please try again.")


def show_menu():
    print("\n" + "="*55)
    print("       English Grammar Quiz App")
    print("="*55)
    print("  1) Start Quiz")
    print("  2) View Scores")
    print("  3) Exit")
    print("="*55)

    while True:
        choice = input("Choose an option (1/2/3): ").strip()
        if choice in ("1", "2", "3"):
            return choice
        print("⚠  Please enter 1, 2, or 3.")


def main():
    while True:
        choice = show_menu()

        if choice == "1":
            player_name = get_player_name()
            score, total = run_quiz(player_name)
            save_score(player_name, score, total)

        elif choice == "2":
            show_scores()

        elif choice == "3":
            print("\n👋  Thanks for playing! Goodbye!\n")
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGoodbye!\n")