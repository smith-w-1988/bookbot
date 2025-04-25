import sys
from stats import word_count, count_of_characters, sorted_list_func

def get_book_text(filepath):
    with open(filepath) as f:
        file_text = f.read()
    return file_text



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    dictionary_of_words = count_of_characters(book_text)
    sorted_list =sorted_list_func(dictionary_of_words)
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print(f"----------- Word Count ----------")
    word_count(book_text)
    print(f"--------- Character Count -------")
    for val in sorted_list:
        if val["char"].isalpha():
            print(f"{val["char"]}: {val["num"]}")
    print(f"============= END ===============")

main()