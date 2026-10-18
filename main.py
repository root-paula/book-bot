from stats import count_words, get_char_counts, get_char_frequencies


def get_book_text(filepath: str) -> str:
    with open(filepath) as file:
        return file.read()


def print_report(
    book_path: str, word_count: int, char_frequencies: list[tuple[str, int]]
) -> None:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char, frequency in char_frequencies:
        if char.isalpha():
            print(f"{char}: {frequency}")
    print("============= END ===============")


def main():
    book_filepath = "books/frankenstein.txt"
    book_text = get_book_text(book_filepath)
    word_count = count_words(book_text)
    char_counts = get_char_counts(book_text)
    char_frequencies = get_char_frequencies(char_counts)

    print_report(book_filepath, word_count, char_frequencies)


if __name__ == "__main__":
    main()
