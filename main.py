def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    characters = get_character_count(text)
    print(characters)


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
    

main()