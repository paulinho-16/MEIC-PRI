from imdb import IMDb
import pandas as pd
from requests import get
from bs4 import BeautifulSoup

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







############################ Scraping Cast ############################

# df = pd.read_csv('DeleteColumns.csv', sep=",", low_memory=True)

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

# df = pd.read_csv('ScrapingCast.csv', sep=",", low_memory=True)

# # No start and end year together
# no_start_end_years = df.loc[(df['startYear'].isna() & df['endYear'].isna())]

# # Miniseries or Series without endYear
# no_endYear = df.loc[((df['type'] == "series") | (df['type'] == "miniSeries")) & df['endYear'].isna()]

# # Concatenate without duplicates
# no_years = pd.concat([no_start_end_years,no_endYear]).drop_duplicates().reset_index(drop=True)
# count = 0

# def get_years(imdb_id):
#     print(imdb_id)
#     global count
#     count+=1
#     print(count)
#     try:
#         movie_serie = imdb.get_movie(imdb_id[2:])
#         movie_series_type = no_years.loc[(no_years['imdb_id'] == imdb_id)].iloc[0]['type']
        
#         if ((movie_series_type == 'series')):
#             years = movie_serie['series years']
#             startYear, endYear = years.split("-",1)
#         else:
#             startYear = movie_serie['year']
#             endYear = ""
#         return (startYear, endYear)
#     except Exception as e:
#         print("Exception getting year info from " + imdb_id + ": " + str(e))
#         return ("Not available", "Not available")

# no_years['startYear'], no_years['endYear'] = no_years.apply(lambda x: get_years(x['imdb_id']), axis=1)
# arr1, arr2 = no_years['startYear'].to_numpy(), no_years['endYear'].to_numpy()
# df.loc[df['startYear'].isna(), 'startYear'], df.loc[df['endYear'].isna(), 'endYear'] = arr1, arr2

# # Saves to file
# df.to_csv("ScrapingYears.csv", index=False)





########################### Scraping Episodes ############################

# def get_episodes(imdb_id):
#     url = 'https://www.imdb.com/title/' + imdb_id
#     response = get(url)
#     print(response.text[:250])
#     html_soup = BeautifulSoup(response.text, 'html.parser')
#     episode_containers = html_soup.find_all('div', class_='SubNav__SubNavContainer-sc-11106ua-1 hDUKxp')
#     episode_number = episode_containers[0].find('span', class_ = 'EpisodeNavigationForSeries__EpisodeCountSpan-sc-1aswzzz-3 jbsbnI').text
#     print(episode_number)


# df = pd.read_csv('ScrapingYears.csv', sep=",", low_memory=True)

# # TODO - BeautifulSoup

# # Saves to file
# df.to_csv("ScrapingEpisodes.csv", index=False)
# get_episodes('tt7767422')





########################### Scraping Runtimes ############################

# df = pd.read_csv('DeleteColumns.csv', sep=",", low_memory=True) # TODO: Mudar para ScrapingEpisodes

# no_runtime = df.loc[df['runtime']=="\\N"]

# def get_runtimes(imdb_id):
#     print(imdb_id)
#     try:
#         movie_serie = imdb.get_movie(imdb_id[2:])
#         runtimes = movie_serie['runtimes']
#         return runtimes[0]
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
#     except Exception as e:  
#         print("Exception getting language info from " + imdb_id + ": " + str(e))
#         return "Not available"

# no_language['language'] = no_language.apply(lambda x: get_languages(x['imdb_id']), axis=1)
# arrLanguages = no_language['language'].to_numpy()
# df.loc[df['language'] == "-", 'language'] = arrLanguages

# Saves to file
# df.to_csv("ScrapingLanguage.csv", index=False)


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
