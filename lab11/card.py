from dataclasses import dataclass
from random import shuffle


@dataclass(frozen=True)
class Card:
    suit: str
    rank: str

    def __post_init__(self):
        if self.suit not in ('S', 'H', 'D', 'C'):
            raise ValueError("Suit must be one of 'S', 'H', 'D', 'C'")
        if self.rank not in range(1, 14):
            raise ValueError("rank must be an integer between 1 and 13")

    def __str__(self):
        suit_str = {"S": "♠", "H": "♥", "D": "♦", "C": "♣"}[self.suit]
        rank_str = {1: "A", 11: "J", 12: "Q", 13: "K"}.get(
            self.rank, str(self.rank))
        return f"{rank_str}{suit_str}"


def standard_deck():
    return [Card(suit=s, rank=r) for s in ("SHDC") for r in range(1, 14)]


def shuffled_deck():
    deck = standard_deck()
    shuffle(deck)
    return deck


def deal_one_five_card_hand():
    deck = shuffled_deck()
    return set(deck[:5])
