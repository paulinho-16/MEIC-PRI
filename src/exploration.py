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
plt.title("Column 'type' frequencies")
ax = sns.countplot(x="type", data=df, order = df['type'].value_counts().index)
plt.show()

def get_decade(year):
    year_int = int(year)
    string = str(year_int//10) + "0-" + str(year_int//10) + "9"
    return string

df_copy = df.copy()
df_copy = df_copy.astype({'startYear': str})

df_copy['startYear'] = df_copy['startYear'].apply(lambda x: get_decade(x[:-2]) if x != "nan" else "Not available")





############# StartYear Rating ###############
df_copy = df_copy[df_copy.startYear != "Not available"]

df_copy = df_copy.sort_values('startYear')
sns.boxplot(x=df_copy["startYear"], y=df_copy["rating"])

plt.xlabel('startYear')
plt.ylabel('rating')
plt.title('Evolution of rating over the decades', y=1.1)
plt.show()





df_copy = df.copy()
df_copy = df_copy[df_copy.language != "-"] # TODO: Trocar por Not available

ser = df_copy.groupby('language')['language'].count()
ser = ser.sort_values(ascending=False)
ser['Others'] = ser[9:].sum()
ser = ser.iloc[[0,1,2,3,4,5,6,7,8,-1]]
print(ser)

fig = plt.figure()
ax = fig.add_subplot(111)

ax.pie(ser.values, labels=ser.index, startangle=90, autopct=lambda x:int(x/100.*ser.sum()), pctdistance=0.8, counterclock=False)
ax.legend()
plt.axis('equal')
plt.title('Most used languages', y=1.1)
plt.show()

#################################################

df_copy = df.copy()
df_copy = df_copy[df_copy.language != "-"] # TODO: Trocar por Not available

ser = df_copy.groupby('orign_country')['orign_country'].count()
ser = ser.sort_values(ascending=False)
ser['Others'] = ser[9:].sum()
ser = ser.iloc[[0,1,2,3,4,5,6,7,8,-1]]
print(ser)

fig = plt.figure()
ax = fig.add_subplot(111)

ax.pie(ser.values, labels=ser.index, startangle=90, autopct=lambda x:int(x/100.*ser.sum()), pctdistance=0.8, counterclock=False)
ax.legend()
plt.axis('equal')
plt.title('Most common origin countries', y=1.1)
plt.show()















df_series = df.loc[((df['type'] == 'series') & (df['runtime'] != "\\N"))] #TODO: Substituir por Not Available 
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
