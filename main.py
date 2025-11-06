def get_book_text(path):
    with open(path) as f: # opens file
        file_contents = f.read() # reads the text
    return file_contents # returns text to console

# imports functions from stats.py file
from stats import count_words, character_count

def main():

    # relative path, not home directory like shell/bash
    path_to_file = "books/frankenstein.txt"
    book_text = get_book_text(path_to_file)

    # --- word count ---
    num_words = count_words(book_text) 
    print(f"Found {num_words} total words")

    # --- character count ---
    char_counts = character_count(book_text)
    for char, count in char_counts.items():
        print(f"t : {count}", f"p : {count}", f"c : {count}")


main() 