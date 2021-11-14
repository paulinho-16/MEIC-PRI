from imdb import IMDb
from imdb import IMDbDataAccessError
import pandas as pd
import numpy as np
from pathlib import Path
import logging

# Creating instance of IMDb
imdb = IMDb(reraiseExceptions=True)
logger = logging.getLogger('imdbpy')
logger.disabled = True

datasets_folder = Path("./datasets")

invalid_imdb = []

######################## Scraping Certificate #########################

# df = pd.read_csv(datasets_folder/'cleaning.csv', sep=",", low_memory=True)

# arr = df['imdbID'].to_numpy()

# def get_certificates(imdb_id):
#     try:
#         movie_serie = imdb.get_movie(imdb_id[2:])
#         certificates = movie_serie['certificates']
#         certificates_list = []
#         for cert in certificates:
#             if cert.count(":")>1:
#                 cert_list = cert.split(":",2)
#                 cert_list.pop()
#             else:
#                 cert_list = cert.split(":",1)
#             certificates_list+=cert_list
#         certificates_dict = {certificates_list[i]: certificates_list[i + 1] for i in range(0, len(certificates_list), 2)}
#         return str(certificates_dict)
#     except IMDbDataAccessError:
#         print('Invalid IMDB id')
#         invalid_imdb.append(imdb_id)
#         return "Not available"
#     except Exception:
#         print("Exception getting certificates info from " + imdb_id)
#         return "Not available"

# df['certificate'] = df.apply(lambda x: get_certificates(x['imdbID']), axis=1)
# arrCert = df['certificate'].to_numpy()
# df['certificate'] = arrCert

# Store the invalid IMDbs # TODO: Possibly delete the invalid imdb ids
# print(invalid_imdb)
# np.save("invalid.npy", invalid_imdb)

# # Saves to file
# df.to_csv("ScrapingCertificate.csv", index=False)

########################### Scraping Years ############################

df = pd.read_csv('ScrapingCertificate.csv', sep=",", low_memory=True)

# No start and end year together
no_start_end_years = df.loc[(df['startYear'].isna() & df['endYear'].isna())]

# Miniseries or Series without endYear
no_endYear = df.loc[((df['type'] == "series") | (df['type'] == "miniSeries")) & df['endYear'].isna()]

# Concatenate without duplicates
no_years = pd.concat([no_start_end_years,no_endYear]).drop_duplicates().reset_index(drop=True)
count = 0

def get_years(imdb_id):
    global count
    count+=1
    print(count)
    try:
        movie_serie = imdb.get_movie(imdb_id[2:])
        movie_series_type = no_years.loc[(no_years['imdbID'] == imdb_id)].iloc[0]['type']
        
        if ((movie_series_type == 'series')):
            years = movie_serie['series years']
            startYear, endYear = years.split("-",1)
        else:
            startYear = movie_serie['year']
            endYear = "Not available"
        return pd.Series([startYear, endYear])
    except IMDbDataAccessError:
        print('Invalid IMDB id')
        invalid_imdb.append(imdb_id)
        return "Not available"
    except Exception:
        print("Exception getting years info from " + imdb_id)
        return "Not available"

df[['startYear','endYear']] = df.loc[((df['startYear'].isna() & df['endYear'].isna()) | (((df['type'] == "series") | (df['type'] == "miniSeries")) & df['endYear'].isna()))].apply(lambda x: get_years(x['imdbID']), axis=1)

# Saves to file
df.to_csv("ScrapingYears.csv", index=False)

########################### Scraping Episodes ############################

df = pd.read_csv('ScrapingYears.csv', sep=",", low_memory=True)

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
        
        # printing total episodes of each season
        # traversing each key
        for i in episodes.keys():
            
            # getting total episode in season i
            total_episodes = total_episodes + len(episodes[i])
        
        return str(total_episodes)
    except IMDbDataAccessError:
        print('Invalid IMDB id')
        invalid_imdb.append(imdb_id)
        return "Not available"
    except Exception:
        print("Exception getting certificates info from " + imdb_id)
        return "Not available"

no_episodes['episodes'] = no_episodes.apply(lambda x: get_episodes(x['imdbID']), axis=1)
arrEpisodes = no_episodes['episodes'].to_numpy()

df.loc[(df['episodes'].isna() & ((df['type'] == "series") | (df['type'] == "miniSeries"))), 'episodes'] = arrEpisodes

# Change blanks to Not Available
df.loc[df['episodes'].isna(), 'episodes'] = "Not available"

# Saves to file
df.to_csv("ScrapingEpisodes.csv", index=False)

########################### Scraping Runtimes ############################

df = pd.read_csv('ScrapingEpisodes.csv', sep=",", low_memory=True)

no_runtime = df.loc[df['runtime']=="\\N"]

def get_runtimes(imdb_id):
    try:
        movie_serie = imdb.get_movie(imdb_id[2:])
        runtimes = movie_serie['runtimes']
        return runtimes[0]
    except IMDbDataAccessError:
        print('Invalid IMDB id')
        invalid_imdb.append(imdb_id)
        return "Not available" # 
    except Exception:
        print("Exception getting certificates info from " + imdb_id)
        return "Not available"

no_runtime['runtime'] = no_runtime.apply(lambda x: get_runtimes(x['imdbID']), axis=1)
arrRuntimes = no_runtime['runtime'].to_numpy()
df.loc[df['runtime'] == "\\N", 'runtime'] = arrRuntimes

# Saves to file
df.to_csv("ScrapingRuntimes.csv", index=False)

# TODO: Talvez mudar de string para int

######################## Scraping Origin Country #########################

df = pd.read_csv('ScrapingRuntimes.csv', sep=",", low_memory=True)

no_country = df.loc[df['origin_country']=="-"]

def get_countries(imdb_id):
    try:
        movie_serie = imdb.get_movie(imdb_id[2:])
        origin_country = movie_serie['countries']
        return origin_country[0]
    except IMDbDataAccessError:
        print('Invalid IMDB id')
        invalid_imdb.append(imdb_id)
        return "Not available" 
    except Exception:
        print("Exception getting certificates info from " + imdb_id)
        return "Not available"

no_country['origin_country'] = no_country.apply(lambda x: get_countries(x['imdbID']), axis=1)
arrCountries = no_country['origin_country'].to_numpy()
df.loc[df['origin_country'] == "-", 'origin_country'] = arrCountries

# Saves to file
df.to_csv("ScrapingCountry.csv", index=False)

########################### Scraping Language ############################

df = pd.read_csv('ScrapingCountry.csv', sep=",", low_memory=True)

no_language = df.loc[df['language']=="-"]

def get_languages(imdb_id):
    try:
        movie_serie = imdb.get_movie(imdb_id[2:])
        language = movie_serie['languages']
        return language[0]
    except IMDbDataAccessError:
        print('Invalid IMDB id')
        invalid_imdb.append(imdb_id)
        return "Not available"
    except Exception:
        print("Exception getting certificates info from " + imdb_id)
        return "Not available"

no_language['language'] = no_language.apply(lambda x: get_languages(x['imdbID']), axis=1)
arrLanguages = no_language['language'].to_numpy()
df.loc[df['language'] == "-", 'language'] = arrLanguages

# Saves to file
df.to_csv("ScrapingLanguage.csv", index=False)

############################ Scraping Summary ############################

df = pd.read_csv('ScrapingLanguage.csv', sep=",", low_memory=True)

no_summary = df.loc[(df['summary'] == "-") | (df['summary'] == "Plot unknown.")]

def get_summaries(imdb_id):
    try:
        movie_serie = imdb.get_movie(imdb_id[2:])
        summary = movie_serie['plot']
        return summary[0]
    except IMDbDataAccessError:
        print('Invalid IMDB id')
        invalid_imdb.append(imdb_id)
        return "Not available"
    except Exception:
        print("Exception getting certificates info from " + imdb_id)
        return "Not available"

no_summary['summary'] = no_summary.apply(lambda x: get_summaries(x['imdbID']), axis=1)
arrSummaries = no_summary['summary'].to_numpy()
df.loc[df['summary'].isna(), 'summary'] = arrSummaries

# Saves to file
df.to_csv("ScrapingSummary.csv", index=False)

############################ Scraping Rating #############################

df = pd.read_csv('ScrapingSummary.csv', sep=",", low_memory=True)

no_rating = df.loc[df['rating'].isna()]

def get_ratings(imdb_id):
    try:
        movie_serie = imdb.get_movie(imdb_id[2:])
        rating = movie_serie['rating']
        return rating
    except IMDbDataAccessError:
        print('Invalid IMDB id')
        invalid_imdb.append(imdb_id)
        return "Not available"
    except Exception:
        print("Exception getting certificates info from " + imdb_id)
        return "Not available"

no_rating['rating'] = no_rating.apply(lambda x: get_ratings(x['imdbID']), axis=1)
arrRatings = no_rating['rating'].to_numpy()
df.loc[df['rating'].isna(), 'rating'] = arrRatings

# Saves to file
df.to_csv("ScrapingRating.csv", index=False)

############################ Scraping NumVotes ###########################

df = pd.read_csv('ScrapingRating.csv', sep=",", low_memory=True)

no_numVotes = df.loc[df['numVotes'].isna()]

def get_num_votes(imdb_id):
    try:
        movie_serie = imdb.get_movie(imdb_id[2:])
        numVotes = movie_serie['votes']
        return numVotes
    except IMDbDataAccessError:
        print('Invalid IMDB id')
        invalid_imdb.append(imdb_id)
        return "Not available"
    except Exception:
        print("Exception getting certificates info from " + imdb_id)
        return "Not available"

no_numVotes['numVotes'] = no_numVotes.apply(lambda x: get_num_votes(x['imdbID']), axis=1)
arrVotes = no_numVotes['numVotes'].to_numpy()
df.loc[df['numVotes'].isna(), 'numVotes'] = arrVotes

# Saves to file
df.to_csv("ScrapingNumVotes.csv", index=False)

############################# Scraping Genres ############################

df = pd.read_csv('ScrapingNumVotes.csv', sep=",", low_memory=True)

genres_nulls = df.loc[(df['genres'] == "\\N")]
arr = genres_nulls['imdbID'].to_numpy()

def get_genres(imdb_id):
    try:
        movie_serie = imdb.get_movie(imdb_id[2:])
        genres = movie_serie['genres']
        return genres
    except IMDbDataAccessError:
        print('Invalid IMDB id')
        invalid_imdb.append(imdb_id)
        return "Not available"
    except Exception:
        print("Exception getting certificates info from " + imdb_id)
        return "Not available"
    
genres_nulls['genres'] = genres_nulls.apply(lambda x: get_genres(x['imdbID']), axis=1)
arrGenres = genres_nulls['genres'].to_numpy()
df.loc[df['genres'] == "\\N", 'genres'] = arrGenres

# Saves to file
df.to_csv("ScrapingGenres.csv", index=False)

############################ Scraping Cast ############################

df = pd.read_csv('ScrapingGenres.csv', sep=",", low_memory=True)

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
        invalid_imdb.append(imdb_id)
        return "Not available"
    except Exception:
        print("Exception getting certificates info from " + imdb_id)
        return "Not available"
    return cast_names
    
cast_nulls['cast'] = cast_nulls.apply(lambda x: get_cast(x['imdbID']), axis=1)
arr = cast_nulls['cast'].to_numpy()
df.loc[df['cast'] == "-", 'cast'] = arr

# Saves to file
df.to_csv("final_netflix_list.csv", index=False)

print('################################# INVALID IMDB #########################################')
print(invalid_imdb)