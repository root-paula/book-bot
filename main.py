from stats import count_words, get_char_counts, get_char_frequencies


def get_book_text(filepath: str) -> str:
    with open(filepath) as file:
        return file.read()


def main():
    book_filepath = "books/frankenstein.txt"
    book_text = get_book_text(book_filepath)
    num_words = count_words(book_text)
    char_counts = get_char_counts(book_text)
    char_frequencies = get_char_frequencies(char_counts)

    print(f"Found {num_words} total words")
    print(char_frequencies)


if __name__ == "__main__":
    main()
