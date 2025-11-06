def count_words(file_contents):
    words = file_contents.split()
    return len(words)

def character_count(file_contents):
    file_contents = file_contents.lower()
    # makes everything lowercase
    chars = {}
    for c in file_contents:
        chars[c] = chars.get(c, 0) + 1 
    return chars