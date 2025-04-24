def get_book_text(file_path):
    try:
        with open(file_path) as f:
            file_contents = f.read()
        return file_contents
    except FileNotFoundError:
        print(f"error: the file at '{file_path}' was not found.")
        return None

def book_word_count(book_text):
    words = book_text.split()
    word_count = len(words)
    return word_count

def main():
    file_path = "books/frankenstein.txt"
    book_text = get_book_text(file_path)
    if book_text:
        word_count = book_word_count(book_text)
        print (f"{word_count} words found in the document")
    else:
        print("Could not read the book text. Please check the file path.")

main()