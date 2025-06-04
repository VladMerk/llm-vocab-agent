import csv
from typing import Iterable, List


def load_words_from_csv(path: str) -> List[str]:
    """Load words from a CSV file using the ``word`` column."""
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return [row['word'] for row in reader if row.get('word')]


def filter_known_words(words: Iterable[str], known_words: Iterable[str]) -> List[str]:
    """Return words not present in the collection of known words."""
    known_set = {w.lower() for w in known_words}
    return [w for w in words if w.lower() not in known_set]
