def count_words(text: str) -> int:
    return len(text.split())


def get_char_counts(text: str) -> dict[str, int]:
    char_counts = {}
    for char in text.lower():
        char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts
