from quiz import run_quiz
from scores import show_scores

def show_menu():
    print()
    print("================")
    print("    Quiz App")
    print("================")
    print("1. Start Quiz")
    print("2. View Score History")
    print("3. Exit")
    print()

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1, 2 or 3): ").strip()

        if choice == "1":
            player_name = input("Enter your name: ").strip()
            if not player_name:
                player_name = "Anonymous"
            run_quiz(player_name)

        elif choice == "2":
            show_scores()

        elif choice == "3":
            print()
            print("Goodbye! See you next time.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

main()