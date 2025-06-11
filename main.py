from stats import *

def main(path):
    print("============ BOOKBOT ============")
    print(f'Analyzing book found at {path}')
    text = get_book_text(path)
    word_count = get_words_count(text)
    print("----------- Word Count ----------")
    print(f'Found {word_count} total words')
    char_count = get_characters(text)
    print("--------- Character Count -------")
    for key in char_count:
        if key.isalpha():
            print(f"{key}: {char_count[key]}")
    print("============= END ===============")

main("books/frankenstein.txt")
