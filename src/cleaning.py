from imdb import IMDb
import pandas as pd
from requests import get
from pathlib import Path

# Creating instance of IMDb
imdb = IMDb()

data_folder = Path("./datasets")

# Read the original dataset
df = pd.read_csv(data_folder/'netflix_list.csv', sep=",", low_memory=True)

# Trim Title Spaces
df['title'] = df['title'].str.strip()

# Remove irrelevant types
df = df[df.type != "tvEpisode"]
df = df[df.type != "videoGame"]
df = df[df.type.notnull()]

# Rename Types
df['type'] = df['type'].replace(['tvSeries','tvMiniSeries','tvShort','tvSpecial','tvMovie', 'video'],['series','miniSeries','short','special','movie','animation'])

# Delete Plot and isAdult
df = df.drop(columns=['isAdult', 'plot'])

# Refactor Genres
df['genres'] = df['genres'].apply(lambda x: [i for i in x.split(",")])

# Save the cleaned data to csv
df.to_csv(data_folder/"cleaning.csv", index=False)