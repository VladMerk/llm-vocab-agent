import csv
from llm_vocab_agent.csv_utils import load_words_from_csv, filter_known_words


def test_load_words_from_csv(tmp_path):
    csv_path = tmp_path / "words.csv"
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["word", "translate"])
        writer.writeheader()
        writer.writerow({"word": "sagen", "translate": "говорить"})
        writer.writerow({"word": "gehen", "translate": "идти"})
    assert load_words_from_csv(csv_path) == ["sagen", "gehen"]


def test_filter_known_words():
    words = ["sagen", "gehen", "machen"]
    known = ["gehen"]
    assert filter_known_words(words, known) == ["sagen", "machen"]
