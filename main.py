from stats import count_words, count_chars, generate_sorted_list
import sys


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

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)

    filename = sys.argv[1]

    text = get_book_text(filename)
    num_of_words = count_words(text)
    statistics = generate_sorted_list(count_chars(text))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filename}...\n----------- Word Count ----------")
    print(f"Found {num_of_words} total words")
    print("--------- Character Count -------")

    for item in statistics:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")

    print("============= END ===============")

if __name__ == "__main__":
    main()
