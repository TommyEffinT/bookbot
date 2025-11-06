def get_book_text(path):
    with open(path) as f: # can use with open(path, "r", encoding="utf-8") as f: if encoding issues
        file_contents = f.read() # reads the text
    return file_contents # returns text to console

# imports functions from stats.py file
from stats import count_words, character_count, sort_characters

def main():

    # relative path, not home directory like shell/bash
    path_to_file = "books/frankenstein.txt"
    book_text = get_book_text(path_to_file)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    # --- word count ---
    num_words = count_words(book_text) 
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    # --- character count--- 
    char_counts = character_count(book_text)
    sorted_chars = sort_characters(char_counts)
    print("--------- Character Count -------")
    for char, count in char_counts.items(): 
        e_count = char_counts.get('e', 0)
        t_count = char_counts.get('t', 0) 
    print(f"e: {e_count}")
    print(f"t: {t_count}")


        # print(f"{i['char']} : {i['count']}" for sorted character count)
        # use print(f"{char} : {count}") to print every character and count
        # use for char, count in char_counts.items(): t_count = char_counts.get('t', 0) print(f"'t': {t_count}") for specific character count

main() 