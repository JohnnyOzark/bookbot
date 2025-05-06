def book_word_count(book_text):
    words = book_text.split()
    word_count = len(words)
    return word_count

def count_characters(book_text):
    character_count = {}
    book_lower = book_text.lower()
    for character in book_lower:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    return character_count

def sort_report(character_count):
    chrcnt_list = []
    

    for key in character_count:
        char = key
        num = character_count[key]
        new_dict = {"char": char, "num": num}
        chrcnt_list.append(new_dict)

    def sort_on(dict):
        return dict["num"]
    
    chrcnt_list.sort(reverse=True, key=sort_on)
    return chrcnt_list



    
    