# Lab 09: Towers of Hanoi

A recursive implementation of the classic Towers of Hanoi puzzle using Python.

## What it does
The `hanoi.py` program solves the classic Towers of Hanoi puzzle recursively. Features include:
- Accepts a command-line argument for the number of disks
- Prints each move needed to transfer all disks from the source peg to the destination peg
- Follows the Towers of Hanoi rules (only one disk at a time, never place larger disk on smaller)
- Keeps track of the total number of moves

The program demonstrates:
- Classic recursive problem solving
- Command-line argument handling with `sys.argv`
- Input validation (checking for correct number of arguments and valid positive integers)
- Using a global counter to track state across recursive calls
- Error handling with try/except blocks
