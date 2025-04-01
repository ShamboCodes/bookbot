from stats import get_book_text
from stats import count_chars
from stats import count_words

def main():
    # Get the text from the book
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    
    # Get word count
    word_count = count_words(text)
    print(f"Word count: {word_count}")
    
    # Get character count
    char_counts = count_chars(text)
    print(f"Character counts: {char_counts}")
    # You might want to format this output more nicely

if __name__ == "__main__":
    main()