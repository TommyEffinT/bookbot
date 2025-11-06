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

def sort_characters(character_count):
    chars_list = []
    for char, count in character_count.items():
        if char.isalpha():  # only include a-z
           chars_list.append({"char":char, "count": count})
# sort by descending order of count
    chars_list.sort(reverse=True, key=lambda item: item["count"])
    return chars_list