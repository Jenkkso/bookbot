from stats import word_counter, get_book_text, character_counter, sorted_list
import sys


def main(): # stores the new string into the text object

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(sys.argv[1])
    num_of_words = word_counter(text)
    print(f"Found {num_of_words} total words")
    char_output = character_counter(text)
    updated_list = sorted_list(char_output)

    for items in updated_list:
        char = items["char"]
        num = items["num"]
        if (char.isalpha()):
            print(f"{char}: {num}")


main()
