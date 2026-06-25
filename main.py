from quiz import run_quiz

def show_menu():
    print()
    print("================")
    print("    Quiz App")
    print("================")
    print("1. Start Quiz")
    print("2. Exit")
    print()

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            run_quiz()
        elif choice == "2":
            print()
            print("Goodbye! See you next time.")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

main()