import pandas as pd
import matplotlib.pyplot as plt

markets = pd.read_csv('farmers_markets.csv')
state_counts = markets['State'].value_counts()

state_counts.plot(kind='bar')
plt.xticks(rotation=90)
plt.xlabel('State')
plt.ylabel('Number of Farmers Markets')
plt.title('Farmers Markets by State')
plt.tight_layout()
plt.show()
