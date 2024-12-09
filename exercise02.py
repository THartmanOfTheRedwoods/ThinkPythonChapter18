#!/usr/bin/env python3

def uses_none_book_version(word, forbidden):
    for letter in word.lower():
        if letter in forbidden.lower():
            return False
    return True

# Exercise02
def uses_none_v1(word, forbidden):
    word_letters = set(word.lower())
    forbidden_letters = set(forbidden.lower())
    return word_letters.difference(forbidden_letters) == word_letters

def uses_none_v2(word, forbidden):
    word_letters = set(word.lower())
    forbidden_letters = set(forbidden.lower())
    return len(word_letters.intersection(forbidden_letters)) == 0

def main():
    word = 'Apple'
    forbidden = 'cdmntr'
    print(
        uses_none_book_version(word, forbidden),
        uses_none_v1(word, forbidden),
        uses_none_v2(word, forbidden))
    word = 'Hello'
    forbidden = 'aeiouy'
    print(
        uses_none_book_version(word, forbidden),
        uses_none_v1(word, forbidden),
        uses_none_v2(word, forbidden))

if __name__ == '__main__':
    main()