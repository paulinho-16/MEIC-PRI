import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import seaborn as sns


datasets_folder = Path("./datasets")

df = pd.read_csv(datasets_folder/'cleaning.csv', sep=",", low_memory=True) # TODO: Mudar para final_netflix_list.csv

# Column 'type' Bar Chart
# plt.title("Column 'type' frequencies")
# ax = sns.countplot(x="type", data=df, order = df['type'].value_counts().index)
# plt.show()


# y_mean = [np.mean(df['rating'])]*len(df['startYear'])

# plt.plot(df['startYear'], y_mean, color='red', marker='o')
plt.scatter(df['startYear'], df['rating'], marker='o');
plt.title('Evolution of number of episodes', fontsize=14)
plt.xlabel('Release Year', fontsize=10)
plt.ylabel('Number of Episodes', fontsize=10)
plt.grid(True)
plt.show()


result = df.groupby('startYear').mean()

plt.plot(result.index, result['rating'])
plt.xlabel('startYear')
plt.ylabel('rating')
plt.title('Release Year vs Rating', y=1.1)
plt.grid()
plt.show()