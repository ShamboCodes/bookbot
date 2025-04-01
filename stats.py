def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    # Convert to lowercase
    text = text.lower()
    # Initialize empty dictionary
    char_dict = {}
    # Count each character
    for char in text:
        char_dict[char] = char_dict.get(char, 0) + 1
    return char_dict