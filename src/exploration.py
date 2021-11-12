import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import seaborn as sns
import plotly.graph_objects as go
import statistics


datasets_folder = Path("./datasets")

df = pd.read_csv(datasets_folder/'cleaning.csv', sep=",", low_memory=True) # TODO: Mudar para final_netflix_list.csv

# Column 'type' Bar Chart
# plt.title("Column 'type' frequencies")
# ax = sns.countplot(x="type", data=df, order = df['type'].value_counts().index)
# plt.show()


# y_mean = [np.mean(df['rating'])]*len(df['startYear'])

# plt.plot(df['startYear'], y_mean, color='red', marker='o')
# plt.scatter(df['startYear'], df['rating'], marker='o');
# plt.title('Evolution of number of episodes', fontsize=14)
# plt.xlabel('Release Year', fontsize=10)
# plt.ylabel('Number of Episodes', fontsize=10)
# plt.grid(True)
# plt.show()

# def get_decade(year):
    
# decades = []
# ratings = []

# decades[get_decade(year)]

# plt.plot(result.index, result['rating'])
# plt.xlabel('startYear')
# plt.ylabel('rating')
# plt.title('Release Year vs Rating', y=1.1)
# plt.grid()
# plt.show()

# sns.boxplot( x=df["startYear"], y=df["rating"] )
# plt.show()

df_series = df.loc[((df['type'] == 'series') & (df['runtime'] != "\\N"))] #TO-DO: Substituir por Not Available 
df_movie = df.loc[((df['type'] == 'movie') & (df['runtime'] != "\\N"))]
df_miniseries = df.loc[((df['type'] == 'miniSeries') & (df['runtime'] != "\\N"))]
df_short = df.loc[((df['type'] == 'short') & (df['runtime'] != "\\N"))]
df_special = df.loc[((df['type'] == 'special') & (df['runtime'] != "\\N"))]

# print(statistics.mean(pd.to_numeric(df_video['runtime'])))

table_mean = go.Figure(data = go.Table(header = dict(values = ['', 'Mean']),
                    cells = dict(values = [['Rating', 'MiniSeries Runtime', 'Movies Runtime', 'Series Runtime', 'Shorts Runtime', 'Special Runtime'], [pd.to_numeric(df['rating']).mean(), statistics.mean(pd.to_numeric(df_miniseries['runtime'])), statistics.mean(pd.to_numeric(df_movie['runtime'])), statistics.mean(pd.to_numeric(df_series['runtime'])), statistics.mean(pd.to_numeric(df_short['runtime'])), statistics.mean(pd.to_numeric(df_special['runtime']))]])))

table_mean.show()

table_max = go.Figure(data = go.Table(
                    cells = dict(values = [['Min Rating', 'Max Rating'], [pd.to_numeric(df['rating']).min(), pd.to_numeric(df['rating']).max()]])))

table_max.show()