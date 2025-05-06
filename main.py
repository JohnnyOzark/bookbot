import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(file_path):
    try:
        with open(file_path) as f:
            file_contents = f.read()
        return file_contents
    except FileNotFoundError:
        print(f"error: the file at '{file_path}' was not found.")
        return None

from stats import book_word_count
from stats import count_characters
from stats import sort_report

def main():
    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    
    if book_text:
        word_count = book_word_count(book_text)
        char_counts = count_characters(book_text)
        char_count_ordered = sort_report(char_counts)
        print(f"============ BOOKBOT ============")
        print(f"Analysing book found at {file_path}...")
        print(f"------------ Word Count ------------")
        print(f"Found {word_count} total words")
        print(f"--------- Character Count -------")
        for item in char_count_ordered:
            char = item["char"]
            if char.isalpha():
                num = item["num"]
                print(f"{char}: {num}")
        print("============= END =============")
    else:
        print("Could not read the book text. Please check the file path.")

main()