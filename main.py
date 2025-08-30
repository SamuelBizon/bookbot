import sys
from stats import get_num_words
from stats import count_characters
from stats import sort_dictionary

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]

    text = get_book_text(filepath)
    num_words = get_num_words(text)
    char_count = count_characters(text)
    sorted_list_of_directories = sort_dictionary(char_count)


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dir in sorted_list_of_directories:
        print(f"{dir["char"]}: {dir["num"]}")


main()
