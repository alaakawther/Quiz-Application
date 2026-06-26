def get_valid_answer(num_options):
    """
    Keeps asking until the user enters a valid number choice.
    num_options: how many choices exist (e.g. 3)
    """
    valid = [str(i) for i in range(1, num_options + 1)]

    while True:
        answer = input(f"Your answer (1-{num_options}): ").strip()

        if answer in valid:
            return answer

        if answer == "":
            print(f"  ⚠ Please enter a number between 1 and {num_options}.")
        else:
            print(f"  ⚠ '{answer}' is not valid. Enter a number between 1 and {num_options}.")