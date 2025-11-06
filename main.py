def get_book_text(path):
    with open(path) as f: # can use with open(path, "r", encoding="utf-8") as f: if encoding issues
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

    # --- specific character count --- 
    char_counts = character_count(book_text)
    for char, count in char_counts.items():
        t_count = char_counts.get('t', 0)
        p_count = char_counts.get('p', 0)
        c_count = char_counts.get('c', 0)

    print(f"'t': {t_count}")
    print(f"'p': {p_count}")
    print(f"'c': {c_count}")
        
        # use print(f"{char} : {count}") to print every character and count

main() 