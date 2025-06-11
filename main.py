def get_book_text(path):
    with open(path) as f:
        contents = f.read()

    return contents

def get_words_count(text):
    return len(text.split())

def main():
    text = get_book_text("books/frankenstein.txt")
    word_count = get_words_count(text)
    print(f'{word_count} words found in the document')

main()
