from collections import Counter

def get_book_text(path):
    with open(path) as f:
        contents = f.read()

    return contents

def get_words_count(text):
    return len(text.split())

def get_characters(text):
    text = text.lower()
    char_count = Counter(text)
    sorted_char_count = dict(sorted(char_count.items(), key=lambda x:x[1], reverse=True))
    return sorted_char_count    