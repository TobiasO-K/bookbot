import sys

from stats import get_book_text

from stats import num_words

from stats import count_characters

from stats import sorted_hi_lo_list

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

filepath = sys.argv[1]


def main():
    text = get_book_text(filepath)
    word_count = num_words(filepath)
    

    
    character_list = count_characters(text)
    
    sorted_list = sorted_hi_lo_list(character_list)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        char = item["char"]
        num = item["num"]
        if char.isalpha():
            
            
            print(f"{char}:", num)
    print("============= END ===============")


main()

