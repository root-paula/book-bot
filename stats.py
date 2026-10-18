def count_words(text: str) -> int:
    return len(text.split())


def get_char_counts(text: str) -> dict[str, int]:
    char_counts = {}
    for char in text.lower():
        char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts


def sort_on(char_count: tuple[str, int]) -> int:
    return char_count[1]


def get_char_frequencies(char_counts: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(char_counts.items(), reverse=True, key=sort_on)
