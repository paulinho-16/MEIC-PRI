from imdb import IMDb
import pandas as pd

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

# df['type'] = df['type'].replace(['tvSeries','tvMiniSeries','tvShort','tvSpecial','tvMovie'],['series','miniSeries','short','special','movie'])

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
#         return "-"
#     return cast_names
    
# cast_nulls['cast'] = cast_nulls.apply(lambda x: get_cast(x['imdb_id']), axis=1)
# arr = cast_nulls['cast'].to_numpy()
# df.loc[df['cast'] == "-", 'cast'] = arr
# print(df.loc[df['cast'] == "-"])

# # Saves to file
# df.to_csv("ScrapingCast.csv", index=False)

########################### Scraping Years ############################

df = pd.read_csv('ScrapingCast.csv', sep=",", low_memory=True)

no_years = df.loc[(df['startYear'].isna() & df['endYear'].isna()) | (((df['type'] == "series") | (df['type'] == "miniSeries")) & (df['endYear'].isna()))]

def get_years(imdb_id):
    print(imdb_id)
    try:
        movie_serie = imdb.get_movie(imdb_id[2:])
        movie_series_type = no_years.loc[(no_years['imdb_id'] == imdb_id)].iloc[0]['type'] # Ir buscar o type em string

        print(movie_series_type)
        
        if ((movie_series_type == 'series') | (movie_series_type == 'miniSeries')):
            years = movie_serie['series years']
            startYear, endYear = years.split("-",1)
        else:
            startYear = movie_serie['year']
            endYear = ""
        return (startYear, endYear)
    except Exception as e:
        print("Exception getting year info from " + imdb_id + ": " + str(e))
        return ("-", "-")

print("# Series")
print(get_years("tt4052886")) # series
print("# Movie")
print(get_years("tt1488589")) # movie
print("# MiniSerie")
print(no_years.loc[(no_years['imdb_id'] == 10048342)])
print(get_years("tt12837400")) # miniSeries
print("# Short")
nova = df.loc[(df['startYear'].isna() & df['endYear'].isna() & (df['type'] == 'short')) | (df['type'] == 'series')]
print(nova.loc[df['type'] == 'short'])
print(df.loc[(df['startYear'].isna() & df['endYear'].isna() & (df['type'] == 'short')) | (df['type'] == 'series')])
print(no_years.loc[(no_years['imdb_id'] == 13871260)]) # TODO: Devia entrar no filtro e não entra
print(get_years("tt13871260")) # short
print("# Special")
print(get_years("tt13567480")) # special
print("# Video")
print(get_years("tt1107365")) # video

# Saves to file
# df.to_csv("ScrapingYears.csv", index=False)

########################### Scraping Episodes ############################

# df = pd.read_csv('ScrapingYears.csv', sep=",", low_memory=True)

# # TODO - BeautifulSoup

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
#     except Exception as e:  
#         print("Exception getting runtime info from " + imdb_id + ": " + str(e))
#         return "Not available"

# no_runtime['runtime'] = no_runtime.apply(lambda x: get_runtimes(x['imdb_id']), axis=1)
# arrRuntimes = no_runtime['runtime'].to_numpy()
# df.loc[df['runtime'] == "\\N", 'runtime'] = arrRuntimes

# print(arrRuntimes)
# print("-------------------------------------")
# print(df.loc[df['runtime'] == "\\N", 'runtime'])

# Saves to file
# df.to_csv("ScrapingRuntimes.csv", index=False)

# print(get_runtimes("tt2403776"))

# TODO: Talvez mudar de string para int




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
