from datetime import datetime
start = datetime.now()
def reverse_vowels(string):
    string = list(string)
    vowels = []
    indexes = []

    for index, letter in enumerate(string):
        if letter in VOWELS:
            vowels.append(letter)
            indexes.append(index)
            print vowels
            print indexes

    for i, char in zip(indexes, reversed(vowels)):
        string[i] = char

    return ''.join(string)
reverse_vowels('Mohan')
