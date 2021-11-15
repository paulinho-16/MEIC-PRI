from imdb import IMDb
from imdb import IMDbDataAccessError
import pandas as pd
import numpy as np
from pathlib import Path
import logging
import math

# Creating instance of IMDb
imdb = IMDb(reraiseExceptions=True)
logger = logging.getLogger('imdbpy')
logger.disabled = True

datasets_folder = Path("./datasets")

######################## Scraping Certificate #########################

df = pd.read_csv(datasets_folder/'cleaning.csv', sep=",", low_memory=True)

arr = df['imdbID'].to_numpy()

def get_certificates(imdb_id):
    try:
        movie_serie = imdb.get_movie(imdb_id[2:])
        certificates = movie_serie['certificates']
        certificates_list = []
        for cert in certificates:
            if cert.count(":")>1:
                cert_list = cert.split(":",2)
                cert_list.pop()
            else:
                cert_list = cert.split(":",1)
            certificates_list+=cert_list
        certificates_dict = {certificates_list[i]: certificates_list[i + 1] for i in range(0, len(certificates_list), 2)}
        return str(certificates_dict)
    except IMDbDataAccessError:
        print('Invalid IMDB id')
        return "Not available"
    except Exception:
        print("Exception getting certificates info from " + imdb_id)
        return "Not available"

df['certificate'] = df.apply(lambda x: get_certificates(x['imdbID']), axis=1)
arrCert = df['certificate'].to_numpy()
df['certificate'] = arrCert

########################### Scraping Years ############################

# No start and end year together
no_start_end_years = df.loc[(df['startYear'].isna() & df['endYear'].isna())]

# Miniseries or Series without endYear
no_endYear = df.loc[((df['type'] == "series") | (df['type'] == "miniSeries")) & df['endYear'].isna()]

# Concatenate without duplicates
no_years = pd.concat([no_start_end_years, no_endYear]).drop_duplicates().reset_index(drop=True)

def get_years(imdb_id):
    try:
        movie_serie = imdb.get_movie(imdb_id[2:])
        movie_series_type = no_years.loc[(no_years['imdbID'] == imdb_id)].iloc[0]['type']
        if ((movie_series_type == 'series')):
            years = movie_serie['series years']
            startYear, endYear = years.split("-",1)
            if endYear=="":
                endYear="Not available"
        else:
            startYear = movie_serie['year']
            endYear = "Not available"
        return pd.Series([startYear, endYear])
    except IMDbDataAccessError:
        print('Invalid IMDB id')
        return pd.Series(["Not available", "Not available"])
    except Exception as e:
        print("Exception getting years info from " + imdb_id + " " + str(e))
        return pd.Series(["Not available", "Not available"])

def change_type(startYear, endYear):
    if (not math.isnan(startYear)):
        startYear = float(startYear)
        startYearStr = str(int(startYear))
    else:
        startYearStr = "Not available"
    if (not math.isnan(endYear)):
        endYear = float(endYear)
        endYearStr =  str(int(endYear))
    else:
        endYearStr = "Not available"
    return pd.Series([startYearStr, endYearStr])

df[['startYear','endYear']] = df.apply(lambda x: get_years(x['imdbID']) if (x['imdbID'] in no_years['imdbID'].values) else change_type(x['startYear'], x['endYear']), axis=1)

########################### Scraping Episodes ############################

# All series and miniSeries
series_miniseries = df.loc[(df['type'] == "series") | (df['type'] == "miniSeries")]

# Miniseries or Series without endYear
no_episodes = series_miniseries.loc[series_miniseries['episodes'].isna()]

def get_episodes(imdb_id):
    total_episodes = 0

    try:
        # getting information
        series = imdb.get_movie(imdb_id[2:])
        
        # adding new info set
        imdb.update(series, 'episodes')
        
        # getting episodes of the series
        episodes = series.data['episodes']
        
        # printing total episodes of each season traversing each key
        for i in episodes.keys():
            
            # getting total episode in season i
            total_episodes = total_episodes + len(episodes[i])
        
        return str(total_episodes)
    except IMDbDataAccessError:
        print('Invalid IMDB id')
        return "Not available"
    except Exception:
        print("Exception getting episodes info from " + imdb_id)
        return "Not available"

def change_episodes(episodes):
    if (not math.isnan(episodes)):
        episodes = float(episodes)
        episodesStr = str(int(episodes))
    else:
        episodesStr = "Not available"
    return pd.Series([episodesStr])

df["episodes"] = df.apply(lambda x: get_episodes(x['imdbID']) if (x['imdbID'] in no_episodes['imdbID'].values) else change_episodes(x['episodes']), axis=1)

########################### Scraping Runtimes ############################

no_runtime = df.loc[df['runtime']=="\\N"]

def get_runtimes(imdb_id):
    try:
        movie_serie = imdb.get_movie(imdb_id[2:])
        runtimes = movie_serie['runtimes']
        return runtimes[0]
    except IMDbDataAccessError:
        print('Invalid IMDB id')
        return "Not available"
    except Exception:
        print("Exception getting runtimes info from " + imdb_id)
        return "Not available"

no_runtime['runtime'] = no_runtime.apply(lambda x: get_runtimes(x['imdbID']), axis=1)
arrRuntimes = no_runtime['runtime'].to_numpy()
df.loc[df['runtime'] == "\\N", 'runtime'] = arrRuntimes

######################## Scraping Origin Country #########################

no_country = df.loc[df['originCountry']=="-"]

def get_countries(imdb_id):
    try:
        movie_serie = imdb.get_movie(imdb_id[2:])
        origin_country = movie_serie['countries']
        return origin_country[0]
    except IMDbDataAccessError:
        print('Invalid IMDB id')
        return "Not available" 
    except Exception:
        print("Exception getting countries info from " + imdb_id)
        return "Not available"

no_country['originCountry'] = no_country.apply(lambda x: get_countries(x['imdbID']), axis=1)
arrCountries = no_country['originCountry'].to_numpy()
df.loc[df['originCountry'] == "-", 'originCountry'] = arrCountries

########################### Scraping Language ############################

no_language = df.loc[df['language']=="-"]

def get_languages(imdb_id):
    try:
        movie_serie = imdb.get_movie(imdb_id[2:])
        language = movie_serie['languages']
        return language[0]
    except IMDbDataAccessError:
        print('Invalid IMDB id')
        return "Not available"
    except Exception:
        print("Exception getting languages info from " + imdb_id)
        return "Not available"

no_language['language'] = no_language.apply(lambda x: get_languages(x['imdbID']), axis=1)
arrLanguages = no_language['language'].to_numpy()
df.loc[df['language'] == "-", 'language'] = arrLanguages

############################ Scraping Summary ############################

no_summary = df.loc[(df['summary'] == "-") | (df['summary'] == "Plot unknown.")]

def get_summaries(imdb_id):
    try:
        movie_serie = imdb.get_movie(imdb_id[2:])
        summary = movie_serie['plot']
        return summary[0]
    except IMDbDataAccessError:
        print('Invalid IMDB id')
        return "Not available"
    except Exception:
        print("Exception getting summary info from " + imdb_id)
        return "Not available"

no_summary['summary'] = no_summary.apply(lambda x: get_summaries(x['imdbID']), axis=1)
arrSummaries = no_summary['summary'].to_numpy()
df.loc[(df['summary'] == "-") | (df['summary'] == "Plot unknown."), 'summary'] = arrSummaries

# Delete some repeated rows and replace some summaries
df = df.drop(df.loc[(df['imdbID'] == "tt14671790") | (df['imdbID'] == "tt14721908")].index)
df['summary'] = df['summary'].replace(['Plot kept under wraps.','NA.','Plot unknown.'],['Plot under wraps.','Not available','Not available'])

############################ Scraping Rating #############################

no_rating = df.loc[df['rating'].isna()]

def get_ratings(imdb_id):
    try:
        movie_serie = imdb.get_movie(imdb_id[2:])
        rating = movie_serie['rating']
        return rating
    except IMDbDataAccessError:
        print('Invalid IMDB id')
        return "Not available"
    except Exception:
        print("Exception getting rating info from " + imdb_id)
        return "Not available"

no_rating['rating'] = no_rating.apply(lambda x: get_ratings(x['imdbID']), axis=1)
arrRatings = no_rating['rating'].to_numpy()
df.loc[df['rating'].isna(), 'rating'] = arrRatings

############################ Scraping NumVotes ###########################

no_numVotes = df.loc[df['numVotes'].isna()]

def get_num_votes(imdb_id):
    try:
        movie_serie = imdb.get_movie(imdb_id[2:])
        numVotes = movie_serie['votes']
        print("NUMVOTES: " + str(numVotes))
        return str(numVotes)
    except IMDbDataAccessError:
        print('Invalid IMDB id')
        return "Not available"
    except Exception:
        print("Exception getting numVotes info from " + imdb_id)
        return "Not available"

def change_numVotes(numVotes):
    if (not math.isnan(numVotes)):
        numVotes = float(numVotes)
        numVotesStr = str(int(numVotes))
    else:
        numVotesStr = "Not available"
    return pd.Series([numVotesStr])

df['numVotes'] = df.apply(lambda x: get_num_votes(x['imdbID']) if (x['imdbID'] in no_numVotes['imdbID'].values) else change_numVotes(x['numVotes']), axis=1)

############################# Scraping Genres ############################

genres_nulls = df.loc[(df['genres'] == "['\\\\N']")]
arr = genres_nulls['imdbID'].to_numpy()

def get_genres(imdb_id):
    try:
        movie_serie = imdb.get_movie(imdb_id[2:])
        genres = movie_serie['genres']
        return str(genres)
    except IMDbDataAccessError:
        print('Invalid IMDB id')
        return "Not available"
    except Exception:
        print("Exception getting genres info from " + imdb_id)
        return "Not available"

df['genres'] = df.apply(lambda x: get_genres(x['imdbID']) if (x['imdbID'] in genres_nulls['imdbID'].values) else x['genres'], axis=1)

############################ Scraping Cast ############################

cast_nulls = df.loc[(df['cast'] == "-")]
arr = cast_nulls['imdbID'].to_numpy()

def get_cast(imdb_id):
    cast_names = []
    try:
        movie_serie = imdb.get_movie(imdb_id[2:])
        cast = movie_serie['cast']
        for person in cast:
            cast_names.append(person['name'])
    except IMDbDataAccessError:
        print('Invalid IMDB id')
        return "Not available"
    except Exception:
        print("Exception getting cast info from " + imdb_id)
        return "Not available"
    return cast_names
    
df['cast'] = df.apply(lambda x: get_cast(x['imdbID']) if (x['imdbID'] in cast_nulls['imdbID'].values) else x['cast'], axis=1)

# Saves to file
df.to_csv(datasets_folder/"final_netflix_list.csv", index=False)