import csv
import matplotlib.pyplot as plt
from collections import Counter
import pandas as pd

with open('farmers_markets.csv', 'r', encoding='utf-8') as file:
    markets = list(csv.DictReader(file))


def california_market_names():
    return [m['MarketName'] for m in markets if m['State'] == 'California']


def alaska_market_names():
    return [m['MarketName'] for m in markets if m['State'] == 'Alaska']


def markets_with_you_tube_west_of_100():
    return [
        (m['MarketName'], m['street'], m['city'], m['zip'])
        for m in markets
        if float(m['x']) < -100 and m['Youtube'] != ''
    ]


def market_counts_by_state():
    return dict(Counter(m['State'] for m in markets))


def plot_market_histogram():
    state_counts = market_counts_by_state()
    plt.bar(state_counts.keys(), state_counts.values())
    plt.xticks(rotation=90)
    plt.xlabel('State')
    plt.ylabel('Number of Farmers Markets')
    plt.title('Farmers Markets by State')
    plt.tight_layout()
    plt.show()


plot_market_histogram()
