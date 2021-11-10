from imdb import IMDb
import pandas as pd
from requests import get

# creating instance of IMDb
imdb = IMDb()


########################## Trim Title Spaces ##########################

# df = pd.read_csv('..\dataset\\netflix_list.csv', sep=",", low_memory=True)

# df['title'] = df['title'].str.strip()
# df.to_csv("TitleSpaceTrim.csv", index=False)


############################ Remove Types #############################

# df = pd.read_csv('TitleSpaceTrim.csv', sep=",", low_memory=True)

# # Remove tvEpisodes
# df = df[df.type != "tvEpisode"]

# # Remove videogame
# df = df[df.type != "videoGame"]

# # Remove blank types
# df = df[df.type.notnull()]

# df.to_csv("RemoveTypes.csv", index=False)


############################ Rename Types #############################

# df = pd.read_csv('RemoveTypes.csv', sep=",", low_memory=True)

# df['type'] = df['type'].replace(['tvSeries','tvMiniSeries','tvShort','tvSpecial','tvMovie', 'video'],['series','miniSeries','short','special','movie','animation'])

# df.to_csv("RenameTypes.csv", index=False)


####################### Delete Plot and isAdult #######################

# df = pd.read_csv('RenameTypes.csv', sep=",", low_memory=True)

# df = df.drop(columns=['isAdult', 'plot'])

# df.to_csv("DeleteColumns.csv", index=False)


########################### Refactor Genres  ##########################

# df = pd.read_csv('DeleteColumns.csv', sep=",", low_memory=True)

# df['genres'] = df['genres'].apply(lambda x: [i for i in x.split(",")])

# df.to_csv("RefactorGenres.csv", index=False)


######################## Scraping Certificate #########################

# df = pd.read_csv('RefactorGenres.csv', sep=",", low_memory=True)  # TODO: Mudar para ScrapingNumVotes

# arr = df["imdb_id"].to_numpy()

# def get_certificates(imdb_id):
#     print(imdb_id)
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
#         return certificates_dict
#     except imdb.IMDbDataAccessError as e:
#         print('Invalid IMDB id')
#         return "Not available" # TODO: possivelmente eliminar do dataset
#     except Exception as e:
#         print("Exception getting certificates info from " + imdb_id)
#         print(str(e))
#         return "Not available"
    
# # df['certificate'] = df.apply(lambda x: get_certificates(x['imdb_id']), axis=1)
# # arrCert = df['certificate'].to_numpy()
# # df.loc[df['certificate'], 'certificates'] = arrCert

# # Saves to file
# # df.to_csv("ScrapingGenres.csv", index=False)

# print(get_certificates("tt3743822"))


############################ Scraping Cast ############################

# df = pd.read_csv('RefactorGenres.csv', sep=",", low_memory=True)

# cast_nulls = df.loc[(df['cast'] == "-")]
# arr = cast_nulls["imdb_id"].to_numpy()

# def get_cast(imdb_id):
#     print(imdb_id)
#     cast_names = []
#     try:
#         movie_serie = imdb.get_movie(imdb_id[2:])
#         cast = movie_serie['cast']
#         for person in cast:
#             cast_names.append(person['name'])
#     except imdb.IMDbDataAccessError as e:
#         print('Invalid IMDB id')
#         return "Not available" # TODO: possivelmente eliminar do dataset
#     except:
#         print("Exception getting info from " + imdb_id)
#         return "Not available"
#     return cast_names
    
# cast_nulls['cast'] = cast_nulls.apply(lambda x: get_cast(x['imdb_id']), axis=1)
# arr = cast_nulls['cast'].to_numpy()
# df.loc[df['cast'] == "-", 'cast'] = arr
# print(df.loc[df['cast'] == "-"])

# # Saves to file
# df.to_csv("ScrapingCast.csv", index=False)


########################### Scraping Years ############################

df = pd.read_csv('ScrapingCast.csv', sep=",", low_memory=True)

# No start and end year together
no_start_end_years = df.loc[(df['startYear'].isna() & df['endYear'].isna())]

# Miniseries or Series without endYear
no_endYear = df.loc[((df['type'] == "series") | (df['type'] == "miniSeries")) & df['endYear'].isna()]

# Concatenate without duplicates
no_years = pd.concat([no_start_end_years,no_endYear]).drop_duplicates().reset_index(drop=True)
count = 0

def get_years(imdb_id):
    print(imdb_id)
    global count
    count+=1
    print(count)
    try:
        movie_serie = imdb.get_movie(imdb_id[2:])
        movie_series_type = no_years.loc[(no_years['imdb_id'] == imdb_id)].iloc[0]['type']
        
        if (movie_series_type == 'series'):
            years = movie_serie['series years']
            print(years)
            startYear, endYear = years.split("-",1)
        else:
            startYear = movie_serie['year']
            endYear = "Not available"
        return (startYear, endYear)
    # except imdb.IMDbDataAccessError as e:
    #     print('Invalid IMDB id')
    #     return "Not available" # TODO: possivelmente eliminar do dataset
    except:
        print("Exception getting year info from " + imdb_id)
    return ("Not available", "Not available")


no_years['startYear'], no_years['endYear'] = no_years.apply(lambda x: get_years(x['imdb_id']), axis=1) # TODO: Corrigir, no count=1664 dá ValueError: too many values to unpack (expected 2) 
arr1, arr2 = no_years['startYear'].to_numpy(), no_years['endYear'].to_numpy()
# df.loc[df['startYear'].isna(), 'startYear'], df.loc[df['endYear'].isna(), 'endYear'] = arr1, arr2
df.loc[(df['startYear'].isna() & df['endYear'].isna()) | (((df['type'] == "series") | (df['type'] == "miniSeries")) & df['endYear'].isna()), 'startYear'], df.loc[(df['startYear'].isna() & df['endYear'].isna()) | (((df['type'] == "series") | (df['type'] == "miniSeries")) & df['endYear'].isna()), 'endYear'] = arr1, arr2

# Saves to file
df.to_csv("ScrapingYears.csv", index=False)


########################### Scraping Episodes ############################

# df = pd.read_csv('ScrapingCast.csv', sep=",", low_memory=True) # TODO: Mudar para ScrapingYears

# # no_episodes = df.loc[df['episodes'].isna() & ((df['type'] == "series") | (df['type'] == "miniSeries"))]

# # All series and miniSeries
# series_miniseries = df.loc[(df['type'] == "series") | (df['type'] == "miniSeries")]

# # Miniseries or Series without endYear
# no_episodes = series_miniseries.loc[series_miniseries['episodes'].isna()]

# # # Concatenate without duplicates
# # no_years = pd.concat([no_start_end_years,no_endYear]).drop_duplicates().reset_index(drop=True)
# # count = 0

# def get_episodes(imdb_id):
#     total_episodes = 0
    
#     print(imdb_id)

#     try:
#         # getting information
#         series = imdb.get_movie(imdb_id[2:])
        
#         # adding new info set
#         imdb.update(series, 'episodes')
        
#         # getting episodes of the series
#         episodes = series.data['episodes']
        
#         # printing total episodes of each season
#         # traversing each key
#         for i in episodes.keys():
            
#             # getting total episode in season i
#             total_episodes = total_episodes + len(episodes[i])
        
#         print('Total episodes: ' + str(total_episodes))
#         return str(total_episodes)
#     # except imdb.IMDbDataAccessError as e:
#     #     print('Invalid IMDB id')
#     #     return "Not available" # TODO: possivelmente eliminar do dataset
#     except:
#         print("Exception getting episodes info from " + imdb_id)
#     return "Not available"


# no_episodes['episodes'] = no_episodes.apply(lambda x: get_episodes(x['imdb_id']), axis=1)
# arrEpisodes = no_episodes['episodes'].to_numpy()

# # print('NAAAAASSS###################')
# # print(df.loc[(df['episodes'].isna() & ((df['type'] == "series") | (df['type'] == "miniSeries"))), 'episodes'])

# # print('\nARRRAYYYYYYYYYYYYYYYYYYYYYYY')
# # print(arrEpisodes)

# df.loc[(df['episodes'].isna() & ((df['type'] == "series") | (df['type'] == "miniSeries"))), 'episodes'] = arrEpisodes

# # Change blanks to Not Available
# df.loc[df['episodes'].isna(), 'episodes'] = "Not available"

# # Saves to file
# df.to_csv("ScrapingEpisodes.csv", index=False)


########################### Scraping Runtimes ############################

# df = pd.read_csv('DeleteColumns.csv', sep=",", low_memory=True) # TODO: Mudar para ScrapingEpisodes

# no_runtime = df.loc[df['runtime']=="\\N"]

# def get_runtimes(imdb_id):
#     print(imdb_id)
#     try:
#         movie_serie = imdb.get_movie(imdb_id[2:])
#         runtimes = movie_serie['runtimes']
#         return runtimes[0]
#     except imdb.IMDbDataAccessError as e:
#         print('Invalid IMDB id')
#         return "Not available" # TODO: possivelmente eliminar do dataset
#     except Exception as e:  
#         print("Exception getting runtime info from " + imdb_id + ": " + str(e))
#         return "Not available"

# no_runtime['runtime'] = no_runtime.apply(lambda x: get_runtimes(x['imdb_id']), axis=1)
# arrRuntimes = no_runtime['runtime'].to_numpy()
# df.loc[df['runtime'] == "\\N", 'runtime'] = arrRuntimes

# print(arrRuntimes)
# print("-------------------------------------")
# print(df.loc[df['runtime'] == "\\N", 'runtime'])

# # Saves to file
# df.to_csv("ScrapingRuntimes.csv", index=False)

# print(get_runtimes("tt2403776"))

# TODO: Talvez mudar de string para int


######################## Scraping Origin Country #########################

# df = pd.read_csv('DeleteColumns.csv', sep=",", low_memory=True) # TODO: Mudar para ScrapingRuntimes

# no_country = df.loc[df['orign_country']=="-"]

# def get_countries(imdb_id):
#     print(imdb_id)
#     try:
#         movie_serie = imdb.get_movie(imdb_id[2:])
#         origin_country = movie_serie['countries']
#         return origin_country[0]
#     except imdb.IMDbDataAccessError as e:
#         print('Invalid IMDB id')
#         return "Not available" # TODO: possivelmente eliminar do dataset
#     except Exception as e:  
#         print("Exception getting runtime info from " + imdb_id + ": " + str(e))
#         return "Not available"

# no_country['origin_country'] = no_country.apply(lambda x: get_countries(x['imdb_id']), axis=1)
# arrCountries = no_country['origin_country'].to_numpy()
# df.loc[df['origin_country'] == "-", 'origin_country'] = arrCountries

# Saves to file
# df.to_csv("ScrapingCountries.csv", index=False)


########################### Scraping Language ############################

# df = pd.read_csv('DeleteColumns.csv', sep=",", low_memory=True) # TODO: Mudar para ScrapingCountries

# no_language = df.loc[df['language']=="-"]

# def get_languages(imdb_id):
#     print(imdb_id)
#     try:
#         movie_serie = imdb.get_movie(imdb_id[2:])
#         language = movie_serie['languages']
#         return language[0]
#     except imdb.IMDbDataAccessError as e:
#         print('Invalid IMDB id')
#         return "Not available" # TODO: possivelmente eliminar do dataset
#     except Exception as e:  
#         print("Exception getting language info from " + imdb_id + ": " + str(e))
#         return "Not available"

# no_language['language'] = no_language.apply(lambda x: get_languages(x['imdb_id']), axis=1)
# arrLanguages = no_language['language'].to_numpy()
# df.loc[df['language'] == "-", 'language'] = arrLanguages

# Saves to file
# df.to_csv("ScrapingLanguage.csv", index=False)


############################ Scraping Summary ############################

# df = pd.read_csv('ScrapingCast.csv', sep=",", low_memory=True) # TODO: Mudar para ScrapingLanguage

# no_summary = df.loc[(df['summary'] == "-") | (df['summary'] == "Plot unknown.")]

# def get_summaries(imdb_id):
#     print(imdb_id)
#     try:
#         movie_serie = imdb.get_movie(imdb_id[2:])
#         summary = movie_serie['plot']
#         return summary[0]
#     except imdb.IMDbDataAccessError as e:
#         print('Invalid IMDB id')
#         return "Not available" # TODO: possivelmente eliminar do dataset
#     except Exception as e:  
#         print("Exception getting summary info from " + imdb_id + ": " + str(e))
#         return "Not available"

# no_summary['summary'] = no_summary.apply(lambda x: get_summaries(x['imdb_id']), axis=1)
# arrSummaries = no_summary['summary'].to_numpy()
# df.loc[df['summary'].isna(), 'summary'] = arrSummaries

#Saves to file
#df.to_csv("ScrapingSummaries.csv", index=False)

# print(get_summaries("tt1136617"))
# print(get_summaries("tt14641788"))


############################ Scraping Rating #############################

# df = pd.read_csv('ScrapingCast.csv', sep=",", low_memory=True) # TODO: Mudar para ScrapingSummary

# no_rating = df.loc[df['rating'].isna()]

# def get_ratings(imdb_id):
#     print(imdb_id)
#     try:
#         movie_serie = imdb.get_movie(imdb_id[2:])
#         rating = movie_serie['rating']
#         print(rating)
#         return rating
#     except imdb.IMDbDataAccessError as e:
#         print('Invalid IMDB id')
#         return "Not available" # TODO: possivelmente eliminar do dataset
#     except Exception as e:  
#         print("Exception getting rating info from " + imdb_id + ": " + str(e))
#         return "Not available"

# no_rating['rating'] = no_rating.apply(lambda x: get_ratings(x['imdb_id']), axis=1)
# arrRatings = no_rating['rating'].to_numpy()
# df.loc[df['rating'].isna(), 'rating'] = arrRatings

# Saves to file
# df.to_csv("ScrapingRating.csv", index=False)


############################ Scraping NumVotes ###########################

# df = pd.read_csv('ScrapingCast.csv', sep=",", low_memory=True) # TODO: Mudar para ScrapingRating

# no_numVotes = df.loc[df['numVotes'].isna()]

# def get_num_votes(imdb_id):
#     print(imdb_id)
#     try:
#         movie_serie = imdb.get_movie(imdb_id[2:])
#         numVotes = movie_serie['votes']
#         print(numVotes)
#         return numVotes
#     except imdb.IMDbDataAccessError as e:
#         print('Invalid IMDB id')
#         return "Not available" # TODO: possivelmente eliminar do dataset
#     except Exception as e:  
#         print("Exception getting numVotes info from " + imdb_id + ": " + str(e))
#         return "Not available"

# # no_numVotes['numVotes'] = no_numVotes.apply(lambda x: get_num_votes(x['imdb_id']), axis=1)
# # arrVotes = no_numVotes['numVotes'].to_numpy()
# # df.loc[df['numVotes'].isna(), 'numVotes'] = arrVotes

# # Saves to file
# # df.to_csv("ScrapingNumVotes.csv", index=False)


############################# Scraping Genres ############################

# df = pd.read_csv('ScrapingCast.csv', sep=",", low_memory=True)  # TODO: Mudar para ScrapingNumVotes

# genres_nulls = df.loc[(df['genres'] == "\\N")]
# arr = genres_nulls["imdb_id"].to_numpy()

# def get_genres(imdb_id):
#     print(imdb_id)
#     genres_names = []
#     try:
#         movie_serie = imdb.get_movie(imdb_id[2:])
#         genres = movie_serie['genres']
#         return genres
#     except imdb.IMDbDataAccessError as e:
#         print('Invalid IMDB id')
#         return "Not available" # TODO: possivelmente eliminar do dataset
#     except:
#         print("Exception getting info from " + imdb_id)
#         return "Not available"
#     return genres_names
    
# genres_nulls['genres'] = genres_nulls.apply(lambda x: get_genres(x['imdb_id']), axis=1)
# arrGenres = genres_nulls['genres'].to_numpy()
# df.loc[df['genres'] == "\\N", 'genres'] = arrGenres

# Saves to file
# df.to_csv("ScrapingGenres.csv", index=False)







# localized title
# original title
# cast
# genres
# runtimes
# countries
# country codes
# language codes
# color info
# aspect ratio
# sound mix
# certificates
# creator
# number of seasons
# rating
# votes
# cover url
# imdbID
# plot outline
# languages
# title
# year
# kind
# series years
# akas
# seasons
# writer          
# distributors
# special effects
# other companies
# plot
