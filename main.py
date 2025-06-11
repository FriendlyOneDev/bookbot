from stats import *

def main():
    text = get_book_text("books/frankenstein.txt")
    word_count = get_words_count(text)
    print(f'{word_count} words found in the document')
    char_count = get_characters(text)
    for key in char_count:
        print(f"'{key}': {char_count[key]}")

main()
