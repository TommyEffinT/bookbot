def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def count_words(text):
    words = text.split()
    return len(words)

def main():
    path_to_file = "books/frankenstein.txt"
    # relative path, not home directory like shell/bash
    book_text = get_book_text(path_to_file)
    num_words = count_words(book_text)
    print(f"Found {num_words} total words")



main() 