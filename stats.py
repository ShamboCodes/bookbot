def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    text = text.lower()
    char_dict = {}
    for char in text:
        char_dict[char] = char_dict.get(char, 0) + 1
    return char_dict

def sort_char_counts(char_dict):
    chars_list = []
    for char, count in char_dict.items():
        char_dict = {"char": char, "count": count}
        chars_list.append(char_dict)
    def sort_on(dict):
        return dict["count"]
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list