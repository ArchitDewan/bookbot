from stats import *
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    filepath = "books/frankenstein.txt"
    file_contents = get_book_text(filepath)
    num_words = countWords(file_contents)
    print(f"Found {num_words} total words")
    num_char = countCharacters(file_contents)
    print(num_char)


main()
        