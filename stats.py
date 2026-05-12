def word_counter(filepath):
    word_list = filepath.split()
    num_words = 0
    for i in range(len(word_list)):
        num_words += 1

    return num_words


def get_book_text(filepath): #reading the file and returns a string
    with open(filepath) as file:
        return file.read()




def character_counter(text):
    character_list = {}

    for letter in text:
        letter = letter.lower()
        if letter in character_list:
            character_list[letter] += 1
        else:
            character_list[letter] = 1

    return character_list


def sorted_list(dictionary):
    char_list = []
    for char in dictionary:
        char_list.append({"char" : char , "num" : dictionary[char]})
    
    def sort_on(item):
        return item["num"]
    
    char_list.sort(reverse=True, key=sort_on)

    return char_list