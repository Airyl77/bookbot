from stats import count_words, count_chars


def get_book_text(file):
    """
    Reads the content of a book file and returns it as a string.
    
    Args:
        file (str): The path to the book file.
        
    Returns:
        str: The content of the book.
    """
    with open(file, 'r', encoding='utf-8') as f:
        return f.read()


def main():

    text = get_book_text("books/frankenstein.txt")
    print(f"{count_words(text)} words found in the document")
    print(count_chars(text))


if __name__ == "__main__":
    main()
