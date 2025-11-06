# Lab 06: Carmen Sandiego

A Carmen Sandiego game!

This program introduced new data structures, multi-file programs, and virtual environments.

## What it does
The `carmen.py` program is a geography guessing game where players try to find Carmen Sandiego. Features include:
- A database of countries with capitals, coordinates, regions, and landmarks (stored in `geography.py`)
- Random country selection for Carmen's location
- Hint system that provides clues about:
  - The country's capital city
  - Geographic region
  - Famous landmarks
  - Distance from Los Angeles (calculated using the haversine formula)
- Input validation to ensure guesses are valid countries
- Continuous gameplay until the player chooses to exit

The program demonstrates:
- Multi-file Python programs with imports
- Complex nested data structures (dictionaries of dictionaries)
- Using external libraries (`haversine` for distance calculations)
- Pattern matching with `match/case` statements
- Working with geographic coordinates