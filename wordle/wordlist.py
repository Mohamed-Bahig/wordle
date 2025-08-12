# wordle/wordlist.py
from pathlib import Path
import random
from typing import List, Set

# Debug line (optional) - you can remove after verifying imports
# print("Loaded wordlist.py from:", __file__)

class WordList:
    """
    Loads a file of candidate words (one per line).
    Stores list for random selection and set for O(1) membership checks.
    """
    def __init__(self, path: Path):
        self.path = Path(path)
        self.words: List[str] = []
        self.word_set: Set[str] = set()
        self._load()

    def _load(self):
        if not self.path.exists():
            raise FileNotFoundError(f"Word list not found at {self.path}")
        with self.path.open("r", encoding="utf-8") as f:
            for line in f:
                w = line.strip().lower()
                if len(w) == 5 and w.isalpha():
                    self.words.append(w)
        if not self.words:
            raise ValueError("No valid 5-letter words found in the dataset.")
        self.word_set = set(self.words)

    def contains(self, word: str) -> bool:
        return word.lower() in self.word_set

    def random_word(self) -> str:
        return random.choice(self.words)

    def size(self) -> int:
        return len(self.words)
