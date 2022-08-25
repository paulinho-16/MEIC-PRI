import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import seaborn as sns
import plotly.graph_objects as go
import statistics
from pathlib import Path
import ast

datasets_folder = Path("./datasets")

Path("plots/").mkdir(parents=True, exist_ok=True)

df = pd.read_csv(datasets_folder/'final_netflix_list.csv', sep=",", low_memory=True)

# Column 'type' Bar Chart
fig = plt.figure()
plt.title("Column 'type' frequencies")
ax = sns.countplot(x="type", data=df, order = df['type'].value_counts().index)
plt.savefig('plots/typeFrequencies')
plt.close(fig)

# Evolution of rating over the decades Box Plot
def get_decade(year):
    year_int = int(year)
    string = str(year_int//10) + "0-" + str(year_int//10) + "9"
    return string

df_copy = df.copy()
df_copy = df_copy.astype({'startYear': str})

df_copy['startYear'] = df_copy['startYear'].apply(lambda x: get_decade(x) if x != "Not available" else "Not available")

df_copy = df_copy[df_copy.startYear != "Not available"]
df_copy = df_copy[df_copy.rating != "Not available"]

df_copy = df_copy.sort_values('startYear')
df_copy["rating"] = df_copy["rating"].astype(float)

fig = plt.figure()
sns.boxplot(x=df_copy["startYear"], y=df_copy["rating"])
plt.xlabel('startYear', y=1.05, fontsize=15, labelpad=15)
plt.ylabel('rating', x=0.7, fontsize=15, labelpad=15)
plt.title('Evolution of rating over the decades', y=1.05, fontsize=20)
fig.set_size_inches(12, 7)
plt.savefig('plots/ratingEvolution.png')
plt.close(fig)

# Distribution of languages Pie Chart
df_copy = df.copy()
df_copy = df_copy[df_copy.language != "Not available"]

ser = df_copy.groupby('language')['language'].count()
ser = ser.sort_values(ascending=False)
ser['Others'] = ser[9:].sum()
ser = ser.iloc[[0,1,2,3,4,5,6,7,8,-1]]

fig = plt.figure()
ax = fig.add_subplot(111)

ax.pie(ser.values, labels=ser.index, startangle=90, autopct=lambda x:int(x/100.*ser.sum()+0.1), pctdistance=0.8, counterclock=False)
ax.legend()
plt.axis('equal')
plt.title('Most used languages', y=1.05, fontsize=20)
fig.set_size_inches(12, 7)
plt.savefig('plots/languagesDistribution.png')
plt.close(fig)

# Distribution of origin countries Pie Chart
df_copy = df.copy()
df_copy = df_copy[df_copy.originCountry != "Not available"] 

ser = df_copy.groupby('originCountry')['originCountry'].count()
ser = ser.sort_values(ascending=False)
ser['Others'] = ser[9:].sum()
ser = ser.iloc[[0,1,2,3,4,5,6,7,8,-1]]

fig = plt.figure()
ax = fig.add_subplot(111)

ax.pie(ser.values, labels=ser.index, startangle=90, autopct=lambda x:int(x/100.*ser.sum()+0.1), pctdistance=0.8, counterclock=False)
ax.legend()
plt.axis('equal')
plt.title('Most common origin countries', y=1.05, fontsize=20)
fig.set_size_inches(14, 7)
plt.savefig('plots/countriesDistribution.png')
plt.close(fig)

# Distribution of genres Bar Chart
df_copy = df.copy()
df_copy = df_copy[df_copy.genres != "Not available"] 

genres = [ast.literal_eval(x) for x in df_copy["genres"]]
genres = [item for sublist in genres for item in sublist]

freq = {}
for item in genres: 
    if (item in freq): 
        freq[item] += 1
    else: 
        freq[item] = 1

genre_list = list(freq.items())
genre_list = sorted(genre_list, key=lambda x: x[1], reverse=True)

keys = [i[0] for i in genre_list[:9]]
values = [i[1] for i in genre_list[:9]]
last_values =  [i[1] for i in genre_list[9:]]

keys.append("Others")
others = sum(last_values[9:])
values.append(others)

fig = plt.figure()
sns.barplot(keys, values)
plt.title('Most common genres', y=1.05, fontsize=20)
plt.xlabel('genres', fontsize=15, labelpad=15)
plt.ylabel('count', fontsize=15, labelpad=15)
fig.set_size_inches(12, 7)
plt.savefig('plots/genresDistribution.png')
plt.close(fig)

# Number of people in the cast
df_copy = df.copy()
df_copy = df_copy[df_copy.cast != "Not available"]
cast = [ast.literal_eval(x) for x in df_copy["cast"]]
cast = [item for sublist in cast for item in sublist]

freq_cast = {}
for item in cast: 
    if (item in freq_cast): 
        freq_cast[item] += 1
    else: 
        freq_cast[item] = 1

cast_list = list(freq_cast.items())
cast_list = sorted(cast_list, key=lambda x: x[1], reverse=True)

keys = [i[0] for i in cast_list[:20]]
values = [i[1] for i in cast_list[:20]]

fig = plt.figure()
sns.barplot(keys, values)
plt.title('Actors with the most participations', y=1.05, fontsize=20)
plt.xlabel('actors', fontsize=15, labelpad=15)
plt.ylabel('count', fontsize=15, labelpad=15)
fig.set_size_inches(34, 7)
plt.savefig('plots/castDistribution.png')
plt.close(fig)

# Table with generic statistics
df_series = df.loc[((df['type'] == 'series') & (df['runtime'] != "Not available") & (df['rating'] != "Not available"))] 
df_movie = df.loc[((df['type'] == 'movie') & (df['runtime'] != "Not available") & (df['rating'] != "Not available"))]
df_miniseries = df.loc[((df['type'] == 'miniSeries') & (df['runtime'] != "Not available") & (df['rating'] != "Not available"))]
df_short = df.loc[((df['type'] == 'short') & (df['runtime'] != "Not available") & (df['rating'] != "Not available"))]
df_special = df.loc[((df['type'] == 'special') & (df['runtime'] != "Not available") & (df['rating'] != "Not available"))]
df_rating = df[df['rating'] != "Not available"] 

statistic_table = go.Figure(data = go.Table(header = dict(values = ['Attribute', 'Value']),
                    cells = dict(values = [['Min Rating', 'Max Rating', 'Mean Rating', 'Mean MiniSeries Runtime', 'Mean Movies Runtime', 'Mean Series Runtime', 'Mean Shorts Runtime', 'Mean Special Runtime', 'Total Genres', 'Total Languages', 'Total Origin Countries', 'Total Actors'],
                    [min(pd.to_numeric(df_rating['rating'])), max(pd.to_numeric(df_rating['rating'])), pd.to_numeric(df_rating['rating']).mean(), statistics.mean(pd.to_numeric(df_miniseries['runtime'])), statistics.mean(pd.to_numeric(df_movie['runtime'])), statistics.mean(pd.to_numeric(df_series['runtime'])), statistics.mean(pd.to_numeric(df_short['runtime'])), statistics.mean(pd.to_numeric(df_special['runtime'])), len(genre_list), df['language'].nunique(), df['originCountry'].nunique(), len(cast_list)]])))

statistic_table.write_image("plots/statisticsTable.png")