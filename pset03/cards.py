from dataclasses import dataclass
from random import shuffle


@dataclass(frozen=True)
class Card:
    suit: str
    rank: int

    def __post_init__(self):
        if self.suit not in ("S", "H", "D", "C"):
            raise ValueError("suit must be one of 'S', 'H', 'D', 'C'")
        if self.rank not in range(1, 14):
            raise ValueError("rank must be an integer between 1 and 13")

    def __str__(self):
        suit_str = {"S": "♠", "H": "♥", "D": "♦", "C": "♣"}[self.suit]
        rank_str = {1: "A", 11: "J", 12: "Q", 13: "K"}.get(
            self.rank, str(self.rank))
        return f"{rank_str}{suit_str}"


def standard_deck():
    return [Card(suit, rank) for suit in "SHDC" for rank in range(1, 14)]


def shuffled_deck():
    cards = standard_deck()
    shuffle(cards)
    return cards


def deal_one_five_card_hand():
    deck = shuffled_deck()
    return set(deck[:5])


def deal(number_of_hands, cards_per_hand):

    deck = shuffled_deck()
    total_cards_needed = number_of_hands * cards_per_hand
    if not isinstance(number_of_hands, int) or not isinstance(cards_per_hand, int):
        raise TypeError(
            "Both number_of_hands and cards_per_hand must be integers")
    if total_cards_needed > 52:
        raise ValueError("Not enough cards in the deck to deal the hands")
    if number_of_hands < 1:
        raise ValueError("number_of_hands must be at least 1")
    if cards_per_hand < 1:
        raise ValueError("cards_per_hand must be at least 1")

    hands = []
    for i in range(number_of_hands):
        hand = set(deck[i * cards_per_hand:(i + 1) * cards_per_hand])
        hands.append(hand)
    return hands


def poker_classification(hand):
    if not isinstance(hand, set):
        raise TypeError("Hand must be a set")
    if len(hand) != 5:
        raise ValueError("Hand must contain exactly 5 cards")
    if not all(isinstance(card, Card) for card in hand):
        raise TypeError("All elements in hand must be Card objects")

    cards = list(hand)
    ranks = sorted([card.rank for card in cards])
    suits = [card.suit for card in cards]

    rank_counts = {}
    for rank in ranks:
        rank_counts[rank] = rank_counts.get(rank, 0) + 1

    count_values = sorted(rank_counts.values(), reverse=True)

    is_flush = len(set(suits)) == 1

    is_straight = False
    if ranks == [1, 10, 11, 12, 13]:
        is_straight = True
    elif ranks[4] - ranks[0] == 4 and len(set(ranks)) == 5:
        is_straight = True
    elif ranks == [1, 2, 3, 4, 5]:
        is_straight = True

    if is_flush and is_straight and ranks == [1, 10, 11, 12, 13]:
        return "Royal Flush"

    if is_flush and is_straight:
        return "Straight Flush"

    if count_values == [4, 1]:
        return "Four of a Kind"

    if count_values == [3, 2]:
        return "Full House"

    if is_flush:
        return "Flush"

    if is_straight:
        return "Straight"

    if count_values == [3, 1, 1]:
        return "Three of a Kind"

    if count_values == [2, 2, 1]:
        return "Two Pair"

    if count_values == [2, 1, 1, 1]:
        return "One Pair"

    return "High Card"
