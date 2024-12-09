#!/usr/bin/env python3

from deck import Deck

class Exercise07(Deck):

    def __init__(self, cards):
        super().__init__(cards)

    def __str__(self):
        #return '\n'.join([str(card) for card in self.cards])
        return '\n'.join(str(card) for card in self.cards)  # Leave the list-comprehension bit off to make a generator.


def main():
    cards = Exercise07.make_cards()
    deck = Exercise07(cards)
    print(deck)

if __name__ == '__main__':
    main()