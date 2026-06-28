def get_valid_answer(num_options):
    valid_choices = [str(i) for i in range(1, num_options + 1)]

    while True:
        answer = input("Your answer: ").strip()

        if answer == "":
            print("⚠  Please enter an answer. Don't leave it blank!")
        elif answer not in valid_choices:
            print(f"⚠  Invalid choice. Please enter a number between 1 and {num_options}.")
        else:
            return answer