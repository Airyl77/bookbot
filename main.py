from stats import count_words
from stats import count_characters
from stats import sort_dict
import sys

def get_book_test(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path=sys.argv[1]
    text = get_book_test(path)
    num_words = count_words(text)
    # print(f"{num_words} words found in the document")

    num_chars = count_characters(text)
    # print(num_chars)

    num_chars_sort=sort_dict(num_chars)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in num_chars_sort:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

main()