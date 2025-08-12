# wordle/game.py
from .wordlist import WordList
from .utils import evaluate_guess, pretty_feedback
from typing import List, Dict

class WordleGame:
    """
    Encapsulates game state:
    - secret: chosen target word
    - attempts: list of dicts { guess, feedback }
    Provides methods to make a guess and print board.
    """
    def __init__(self, wordlist: WordList, max_attempts: int = 6):
        self.wordlist = wordlist
        self.max_attempts = max_attempts
        self.secret = self.wordlist.random_word()
        self.attempts: List[Dict] = []  # each dict: {"guess": str, "feedback": List[str]}

    def make_guess(self, guess_word: str) -> Dict:
        guess_word = guess_word.lower().strip()
        if len(guess_word) != 5 or not guess_word.isalpha():
            raise ValueError("Guess must be exactly 5 alphabetic characters.")
        if not self.wordlist.contains(guess_word):
            raise ValueError("Guess not in dictionary.")
        if len(self.attempts) >= self.max_attempts:
            raise ValueError("No attempts left.")

        feedback = evaluate_guess(self.secret, guess_word)
        self.attempts.append({"guess": guess_word, "feedback": feedback})
        won = all(f == 'G' for f in feedback)
        lost = len(self.attempts) >= self.max_attempts and not won
        return {
            "guess": guess_word,
            "feedback": feedback,
            "pretty": pretty_feedback(guess_word, feedback),
            "won": won,
            "lost": lost,
            "attempts_left": self.max_attempts - len(self.attempts)
        }

    def print_board(self):
        """
        Prints the 6x5 board. For rows not yet used, show empty squares.
        Each used row shows icons and the guessed word.
        """
        empty_row = "⬜⬜⬜⬜⬜"
        for i in range(self.max_attempts):
            if i < len(self.attempts):
                g = self.attempts[i]
                icons = ''.join('🟩' if f=='G' else '🟨' if f=='Y' else '⬛' for f in g["feedback"])
                print(f"{icons}  {g['guess'].upper()}")
            else:
                print(f"{empty_row}  {'-'*5}")
        print()
