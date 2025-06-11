from collections import Counter

def get_book_text(path):
    with open(path) as f:
        contents = f.read()

    return contents

def get_words_count(text):
    return len(text.split())

def get_characters(text):
    text = text.lower()
    return Counter(text)
        