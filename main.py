def get_book_text(file_path):
    try:
        with open(file_path) as f:
            file_contents = f.read()
        return file_contents
    except FileNotFoundError:
        print(f"error: the file at '{file_path}' was not found.")
        return None

def main():
    file_path = "books/frankenstein.txt"
    book_text = get_book_text(file_path)
    if book_text:
        print (book_text)
    else:
        print("Could not read the book text. Please check the file path.")

main()