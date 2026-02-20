from collections import Counter

def countWords(file_contents):
    return len(file_contents.split())

def countCharacters(file_contents):
    result = {}
    file_contents = file_contents.lower()
    for char in file_contents:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result

def sortDict(character_count):
    