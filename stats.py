def count_words(file_contents):
    words = file_contents.split()
    return len(words)

def character_count(file_contents):
    text = file_contents.lower()
    # makes everything lowercase
    chars = {}
    for c in text:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars