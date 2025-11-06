def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents
def main():
    path_to_file = "books/frankenstein.txt"
    
    book_text = get_book_text(path_to_file)
    print(book_text)

main()