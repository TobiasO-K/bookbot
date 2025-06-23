def get_book_text(book):
    with open(book) as f:
        return f.read()

def num_words(book):
    text = get_book_text(book)
    words = text.split() 
    word_count = len(words)
    return word_count


def count_characters(book):
    characters = {}
    book_lower = book.lower()
    for char in book_lower:
        if char not in characters:
            characters[char] = 1
        

        else:
            characters[char] += 1

    return characters


def sorted_hi_lo_list(characters):
    sorted_list = []
    for letter in characters:
        letter_num = characters[letter]
        char_dict = {}
        char_dict["char"] = letter
        char_dict["num"] = letter_num
        sorted_list.append(char_dict)
        
    def sort_on(char_dict):
        return char_dict["num"]

    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list

    