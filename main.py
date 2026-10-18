from stats import count_words


def get_book_text(filepath: str) -> str:
    with open(filepath) as file:
        return file.read()


def main():
    book_filepath = "books/frankenstein.txt"
    book_text = get_book_text(book_filepath)
    num_words = count_words(book_text)
    print(f"Found {num_words} total words")


if __name__ == "__main__":
    main()
