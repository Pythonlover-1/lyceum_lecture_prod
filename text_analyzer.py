from collections import Counter


def count_words(text: str) -> int:
    return len(text.split())


def average_word_length(text: str) -> float:
    words = text.split()
    if not words:
        return 0.0
    return sum(len(w) for w in words) / len(words)


def top_words(text: str, n: int = 3) -> list[tuple[str, int]]:
    words = text.lower().split()
    return Counter(words).most_common(n)
