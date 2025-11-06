# Problem Set 03

This assignment includes:
- Card and poker hand classes with object-oriented design
- Poker game that deals hands and classifies poker hands
- Classes cardio exercises to practice object-oriented programming concepts

## Programs

### cards.py
Defines classes for playing cards and poker hands:
- `Card` class representing individual playing cards
- `Hand` class representing a poker hand with 5 cards
- Methods to classify poker hands (flush, straight, pairs, etc.)
- Hand comparison logic to determine winning hands

### poker_game.py
An interactive poker game program that:
- Prompts the user for the number of players (2-10)
- Deals 5-card hands to each player from a shuffled deck
- Displays each player's hand
- Classifies each hand (e.g., "Pair of Kings", "Flush", "Three of a Kind")
- Validates input and handles errors gracefully
- Supports 'bye' and 'exit' commands to quit

### classes_cardio.py
Object-oriented programming exercises including:
- Defining classes with attributes and methods
- Implementing inheritance and polymorphism
- Creating class methods and static methods
- Working with special methods (`__str__`, `__repr__`, `__eq__`, etc.)
- Practice with encapsulation and data hiding

### cards_test.py
Unit tests for the Card and Hand classes to ensure:
- Proper card creation and validation
- Correct hand classification
- Accurate hand comparison for determining winners
