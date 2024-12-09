#!/usr/bin/env python3
from collections import Counter


def can_spell_v1(letters, word):
    letters = list(letters.lower())
    for letter in word.lower():
        if not letter in letters:
            return False
        letters.remove(letter)
    return True

def can_spell_v2(letters, word):
    w_cntr = Counter(word.lower())
    l_cntr = Counter(letters.lower())
    for k,v in w_cntr.items():
        if not (k in l_cntr and v <= l_cntr[k]):
            return False
    return True

def can_spell_v3(letters, word):
    w_cntr = Counter(word.lower())
    l_cntr = Counter(letters.lower())
    match = {k: v for k,v in w_cntr.items() if k in l_cntr and v <= l_cntr[k] }
    return w_cntr == match

def can_spell_v4(letters, word):
    return Counter(word.lower()) <= Counter(letters.lower())

def main():
    letters = 'tablE'
    word = 'belt'
    print(can_spell_v1(letters, word), can_spell_v2(letters, word), can_spell_v3(letters, word), can_spell_v4(letters, word))
    word = 'beEt'
    print(can_spell_v1(letters, word), can_spell_v2(letters, word), can_spell_v3(letters, word), can_spell_v4(letters, word))

if __name__ == '__main__':
    main()