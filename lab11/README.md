# Lab 11: Playing Cards

Introduction to object-oriented programming with a Card class using dataclasses in Python.

## What it does
The `card.py` program creates a Card class using Python's `@dataclass` decorator. Features include:
- Immutable Card objects (frozen=True) with suit and rank attributes
- Suit validation (must be S, H, D, or C for Spades, Hearts, Diamonds, Clubs)
- Rank validation (must be integer from 1-13, where 1=Ace, 11=Jack, 12=Queen, 13=King)
- Custom string representation showing Unicode card symbols (♠ ♥ ♦ ♣)
- Deck creation and shuffling functionality

The `card_test.py` file contains unit tests to verify the Card class behavior.

The program demonstrates:
- Using `@dataclass` decorator for cleaner class definitions
- Data validation with `__post_init__`
- Creating immutable objects with `frozen=True`
- Custom string representation with `__str__`
- Working with Unicode characters for display
- Unit testing with assertions
