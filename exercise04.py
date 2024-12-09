#!/usr/bin/env python3
from collections import defaultdict

from poker_hand import PokerHand

class Exercise04(PokerHand):
    def __init__(self, player_name, cards):
        super().__init__(player_name, cards)

    def partition_OLD(self):
        """Make a list of four hands, each containing only one suit."""
        hands = []
        for i in range( 4 ):
            hands.append( PokerHand() )

        for card in self.cards:
            hands[card.suit].put_card( card )

        return hands

    def partition(self):
        hands = defaultdict(PokerHand)

        for card in self.cards:
            hands[card.suit].put_card( card )

        return hands


def main():
    cards = Deck.make_cards()
    deck = Deck(cards)
    deck.shuffle()

    hand_cards = []

    for i in range( 7 ):
        card = deck.take_card()
        hand_cards.append(card)

    random_hand = Exercise04('Trevor', hand_cards)

    print( random_hand )
    print('-'*80)

    print('-'*35, ' OLD Style ', '-'*34)
    hand_list = random_hand.partition_OLD()

    for hand in hand_list:
        print( hand )
        print( '-' * 80 )
        print()

    print('-'*35, ' New Style ', '-'*34)
    hand_dict = random_hand.partition()

    for hand in hand_dict.values():
        print( hand )
        print( '-' * 80 )
        print()

if __name__ == '__main__':
    from deck import Deck
    main()