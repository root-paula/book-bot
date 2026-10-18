from stats import chars_dict_to_sorted_list, count_words, get_char_counts


def get_book_text(filepath: str) -> str:
    with open(filepath) as file:
        return file.read()


def main():
    book_filepath = "books/frankenstein.txt"
    book_text = get_book_text(book_filepath)
    num_words = count_words(book_text)
    char_counts = get_char_counts(book_text)
    sorted_chars = chars_dict_to_sorted_list(char_counts)

    print(f"Found {num_words} total words")
    print(sorted_chars)


if __name__ == "__main__":
    main()
