# Lab 10: Family Tree

A Python program that models family relationships using object-oriented programming with a Person class.

## What it does
The `family.py` program defines a `Person` class that models family relationships. Each Person has:
- Name, birth year, death year (optional)
- References to their mother and father (optional)

The class includes methods to determine relationships:
- `is_sibling_of()` - Checks if two people share at least one parent (includes half-siblings)
- `is_parent_of()` - Checks if this person is a parent of another person
- `is_child_of()` - Checks if this person is a child of another person
- Additional relationship methods for grandparents, grandchildren, cousins, aunts/uncles, nieces/nephews

The program demonstrates:
- Object-oriented programming with classes
- Instance attributes and methods
- Modeling complex relationships through object references
- Using `is` operator for object identity comparison
- Logical operations to determine family connections
