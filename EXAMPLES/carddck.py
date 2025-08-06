import random
from card import card
class CardDeck:
  RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
  SUITS = 'Hearts Diamonds Clubs Spades'.split()
    
    def __init__(self):
          self._make_deck()

    def _make_deck(self):
        self.cards = []
        for suit in self.SUITS:
            for ran in self.RANKS:
                self.cards.append(card(ran, suit))