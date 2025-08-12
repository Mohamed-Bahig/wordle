from pathlib import Path
from wordle.wordlist import WordList
from wordle.game import WordleGame

def run_cli():
    data_file = Path(__file__).parent / "data" / "wordlist.txt"
    print("Loading word list...")
    wordlist = WordList(data_file)
    print(f"Loaded {wordlist.size()} valid five-letter words.\n")
    game = WordleGame(wordlist)

    print("Autobot Intelligence Wordle — Guess the 5-letter code.")
    print("You have 6 attempts. Use only valid dataset words.\n")

    while True:
        game.print_board()
        attempt_num = len(game.attempts) + 1
        try:
            guess = input(f"Attempt {attempt_num}/6: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting. May the AllSpark guide you.")
            break

        try:
            res = game.make_guess(guess)
        except ValueError as e:
            print("❌", e)
            continue

        # print feedback for this guess
        print(res["pretty"])
        if res["won"]:
            game.print_board()
            print(f"\n✅ ACCESS GRANTED — Coordinates decrypted in {len(game.attempts)} attempts. 🎉")
            break
        if res["lost"]:
            game.print_board()
            print(f"\n💀 ACCESS DENIED — Out of attempts. The secret was: {game.secret.upper()}")
            break

if __name__ == "__main__":
    run_cli()
