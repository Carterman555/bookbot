import sys

from stats import get_word_count
from stats import get_char_counts
from stats import get_sorted_char_counts

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def print_display_text(file_path, word_count, sorted_char_counts):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("----------- Character Count ----------")

    for char_count in sorted_char_counts:
        print(f"{char_count["char"]}: {char_count["num"]}")


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    text = get_book_text(file_path)

    word_count = get_word_count(text)

    char_counts = get_char_counts(text)
    sorted_char_counts = get_sorted_char_counts(char_counts)

    print_display_text(file_path, word_count, sorted_char_counts)

    