def count_words(book):
    book_split = book.split()
    print(f"Found {len(book_split)} total words")


def count_characters(book):
    character_dictionary = {
        
            'b': 0, 
            'c': 0, 
            'a': 0, 
            'd': 0, 
            'e': 0, 
            'f': 0, 
            'g': 0, 
            'h': 0, 
            'i': 0, 
            'j': 0, 
            'k': 0, 
            'l': 0, 
            'm': 0, 
            'n': 0, 
            'o': 0, 
            'p': 0, 
            'q': 0, 
            'r': 0, 
            's': 0, 
            't': 0, 
            'u': 0, 
            'v': 0, 
            'w': 0, 
            'x': 0, 
            'y': 0, 
            'z': 0
    }


    for word in book:
        word_split = ""
        word_split = word.lower().split()
        for char in word_split:
            if char in character_dictionary:
                character_dictionary[char] += 1
    
    return character_dictionary
        

def sort_on(d):
    return d["num"]

def sorted_dict(count_characters):
    sorted_list = []
    for ch in count_characters:
        sorted_list.append({"char" : ch, "num" : count_characters[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list