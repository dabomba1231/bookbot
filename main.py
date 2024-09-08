def main():
    book_path = input("Input path to book/document. ")
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    characters = get_character_count(text)
    dict_list = get_dict_list(characters)
    dict_list.sort(reverse=True, key=get_value)
    get_report(dict_list, word_count)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    

def get_word_count(text):
    words = text.split()
    count = 0
    for word in words:
        count += 1
    return count


def get_character_count(text):
    text_lowered = text.lower()
    characters = list(text_lowered)
    character_count = {}
    for character in characters:
        if character not in character_count:
            character_count[character] = 0
            character_count[character] += 1
        else:
            character_count[character] += 1
    return character_count
    

def get_dict_list(characters):
    char_list = []
    for k in characters:
        if k.isalpha() == True:
            dict = {}
            dict["character"] =k
            dict["num"] = characters[k]
            char_list.append(dict)
    return char_list


def get_value(dict):
    return dict["num"]


def get_report(dict, word_count):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    for k in dict:
        character = k["character"]
        num = k["num"]
        print(f"The {character} character was found {num} times")
    print("--- End report ---")

main()