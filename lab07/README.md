# Lab 07: Interest Calculator

This lab involves writing a program to track and calculate interest on money using Python.

## What it does
The `interest.py` program calculates investment growth over time. It includes two main functions:

1. `investment_value()` - Calculates the final balance after a specified number of years, considering:
   - Starting balance
   - Interest rate per year
   - Tax rate on earned interest
   - Annual deposits
   - Compound growth over multiple years

2. `years_to_reach_goal()` - Determines how many years it takes to reach a target amount with the same parameters

The program demonstrates:
- Financial calculations with compound interest
- Loop-based accumulation over time
- Using the Babel library to format currency with locale-specific formatting
- Tax-adjusted investment calculations