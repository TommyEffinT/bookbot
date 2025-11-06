def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

from stats import count_words, character_count

def main():
    # relative path, not home directory like shell/bash
    path_to_file = "books/frankenstein.txt"
    book_text = get_book_text(path_to_file)
    
    # --- word count ---
    num_words = count_words(book_text) 
    print(f"Found {num_words} total words")
    # --- character count ---
    for char, count in character_count.items():
        print(f"{char}: {count}")


main() 