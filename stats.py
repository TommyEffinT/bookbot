def count_words(file_contents):
    words = file_contents.split() # splits text into a seperate word strings
    return len(words) # returns the count of strings

def character_count(file_contents):
    file_contents = file_contents.lower() # makes all characters lowercase
    chars = {} 
    for c in file_contents:
        chars[c] = chars.get(c, 0) + 1 
    return chars
# iterates over every word in text and populates blank dict with both char and count.