from enum import Enum


Suit = Enum('Suit', ['diamonds', 'clubs', 'hearts', 'spades'])

class Card:
    def __int__(self, suit: str, number: int):
        self.suit = suit
        self.number = number

class Deck:
    def __init__(self, cards: list[Card]):
        assert len(cards) == 52, "A deck of cards must contain 52 cards."
