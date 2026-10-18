def get_book_text(filepath: str) -> str:
    with open(filepath) as file:
        return file.read()


def main():
    book_filepath = "books/frankenstein.txt"
    book_text = get_book_text(book_filepath)
    print(book_text)


if __name__ == "__main__":
    main()
