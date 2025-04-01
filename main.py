from stats import get_book_text
from stats import count_chars
from stats import count_words
from stats import sort_char_counts
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # Get the text from the book
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    
    # Get word count
    word_count = count_words(text)

    
    # Get character count
    char_counts = count_chars(text)

    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {book_path}...")
    print ("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    # Print sorted list
    sorted_chars = sort_char_counts(char_counts)
    print("--------- Character Count -------")
    for char_dict in sorted_chars:
        if char_dict["char"].isalpha():
            print(f"{char_dict['char']}: {char_dict['count']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()