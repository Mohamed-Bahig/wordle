# wordle/utils.py
from typing import List

def evaluate_guess(secret: str, guess: str) -> List[str]:
    """
    Return feedback per letter: 'G' = green (correct place),
    'Y' = yellow (present, wrong place), 'B' = black/grey (absent).
    Handles repeated letters correctly by consuming matches.
    """
    secret = secret.lower()
    guess = guess.lower()
    assert len(secret) == 5 and len(guess) == 5

    result = ['B'] * 5
    secret_chars = list(secret)

    # First pass: greens (correct position)
    for i in range(5):
        if guess[i] == secret[i]:
            result[i] = 'G'
            secret_chars[i] = None  # consume

    # Second pass: yellows (present but different position)
    for i in range(5):
        if result[i] == 'G':
            continue
        if guess[i] in secret_chars:
            result[i] = 'Y'
            idx = secret_chars.index(guess[i])
            secret_chars[idx] = None

    return result

def pretty_feedback(guess: str, feedback: List[str]) -> str:
    """
    Human-friendly single-line representation.
    Example: 🟩⬛🟨⬛🟩  apple
    """
    symbols = {'G': '🟩', 'Y': '🟨', 'B': '⬛'}
    icons = ''.join(symbols.get(f, '?') for f in feedback)
    return f"{icons}  {guess.upper()}"
