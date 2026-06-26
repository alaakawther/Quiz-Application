from datetime import datetime

def save_score(player_name, score, total):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    result_line = f"Player: {player_name} | Score: {score}/{total} | Date: {timestamp}\n"

    with open("scores.txt", "a") as file:
        file.write(result_line)

    print(f"\n✔ Score saved for {player_name}!")


def show_scores():
    try:
        with open("scores.txt", "r") as file:
            lines = file.readlines()

        if lines:
            print("\n=== Score History ===")
            for line in lines:
                print(line.strip())
        else:
            print("\nNo scores saved yet.")

    except FileNotFoundError:
        print("\nNo score history found. Play a quiz first!")