def word_count(book_text):
    list_of_words = book_text.split()
    print(f"Found {len(list_of_words)} total words")

def count_of_characters(book_text):
    count_dict={
        'a' : 0,
        'b' : 0,
        'c' : 0,
        'd' : 0,
        'e' : 0,
        'f' : 0,
        'g' : 0,
        'h' : 0,
        'i' : 0,
        'j' : 0,
        'k' : 0,
        'l' : 0,
        'm' : 0,
        'n' : 0,
        'o' : 0,
        'p' : 0,
        'q' : 0,
        'r' : 0,
        's' : 0,
        't' : 0,
        'u' : 0,
        'v' : 0,
        'w' : 0,
        'x' : 0,
        'y' : 0,
        'z' : 0,
        ' ' : 0,
        '!' : 0,
        '"' : 0,
        '#' : 0,
        '$' : 0,
        '%' : 0,
        '&' : 0,
        '(' : 0,
        ')' : 0,
        '*' : 0,
        '+' : 0,
        ',' : 0,
        '-' : 0,
        '.' : 0,
        '/' : 0,
        'æ' : 0,
        'â' : 0,
        'ê' : 0,
        'ë' : 0,
        'ô' : 0
    }
    for char in book_text:
        lower_char = char.lower()
        if lower_char in count_dict:
            count_dict[lower_char] += 1
    return count_dict

def sorted_list_func(dictionary_of_chars):
    dictionary_list = []
    for key, value in dictionary_of_chars.items():
        dictionary_list.append({"char": key, "num": value})
    dictionary_list.sort(key=lambda item: item["num"], reverse=True)
    return dictionary_list