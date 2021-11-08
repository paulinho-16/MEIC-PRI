from imdb import IMDb
import pandas as pd

df = pd.read_csv('..\dataset\\netflix_list.csv', sep=",", low_memory=True)

# creating instance of IMDb
imdb = IMDb()

############################ Scraping Cast ############################

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
# df.to_csv("cast.csv", index=False)

#######################################################################

# Removes all TVEpisodes and blank ones
df = df[df.type != "tvEpisode"]
df = df[df.type != "videoGame"]
df = df[df.type.notnull()]

# df.to_csv("RemoveEpisodes.csv", index=False)

############################ Scraping Cast ############################

df = pd.read_csv('..\src\\RemoveEpisodes.csv', sep=",", low_memory=True)

no_years = df.loc[(df['startYear'].isna() & df['endYear'].isna()) | (((df['type'] == "series") | (df['type'] == "miniSeries")) & (df['endYear'].isna()))]

def get_years(imdb_id):
    print(imdb_id)
    try:
        movie_serie = imdb.get_movie(imdb_id[2:])
        movie_series_type = no_years.loc[(no_years['imdb_id'] == imdb_id)] # Ir buscar o type em string

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
print("# miniSerie")
print(get_years("tt10048342")) # miniSeries
print("# Short")
print(get_years("tt3472226")) # short
print("# Special")
print(get_years("tt13567480")) # special
print("# Video")
print(get_years("tt1107365")) # video

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
# production companies
# distributors
# special effects
# other companies
# plot