from datetime import datetime


def save_score(player_name, score, total):
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result_line = (
            f"Player: {player_name} | Score: {score}/{total} | "
            f"Date: {timestamp}\n"
        )
        with open("scores.txt", "a") as file:
            file.write(result_line)
        print(f"✔  Score saved for {player_name}!\n")
    except IOError as e:
        print(f"⚠  Could not save score: {e}\n")


def show_scores():
    print(f"\n{'='*55}")
    print("   High Scores")
    print(f"{'='*55}")
    try:
        with open("scores.txt", "r") as file:
            lines = file.readlines()
            if not lines:
                print("  No scores recorded yet.")
            else:
                for line in lines:
                    print(f"  {line.strip()}")
    except FileNotFoundError:
        print("  No scores recorded yet.")
    print(f"{'='*55}\n")