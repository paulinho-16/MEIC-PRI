from imdb import IMDb
import pandas as pd

df = pd.read_csv('..\dataset\\netflix_list.csv', sep=",", low_memory=True)

# creating instance of IMDb
imdb = IMDb()

# Fill Cast
cast_nulls = df.loc[(df['cast'] == "-")]
arr = cast_nulls["imdb_id"].to_numpy()

def get_cast(imdb_id):
    print(imdb_id)
    cast_names = []
    try:
        movie_serie = imdb.get_movie(imdb_id[2:])
        cast = movie_serie['cast']
        for person in cast:
            cast_names.append(person['name'])
    except:
        print("Exception getting info from tt" + imdb_id)
        return "-"
    return cast_names
    
cast_nulls['cast'] = cast_nulls.apply(lambda x: get_cast(x['imdb_id']), axis=1)

# print(cast_nulls)
    
arr = cast_nulls['cast'].to_numpy()

df.loc[df['cast'] == "-", 'cast'] = arr

print(df.loc[df['cast'] == "-"])

df.to_csv("cast.csv", index=False)

# id
code = "6468322"
 
# getting information
# series = ia.get_movie(code)

# for i in series.data:
#     print(i)







# print("TITLE: " + series['original title'])

# print('Genres:')
# for genre in series['genres']:
#     print(genre)


# df["cast"].replace({"-": cast_names}, inplace=True)

# print("SEASONS: " + str(series['seasons']))

# print('CERTIFICATES: ')
# cert_list = series['certificates']
# certificates = {}

# for cert in cert_list:
#     splitted_cert = cert.split(':')
#     certificates[splitted_cert[0]] = splitted_cert[1]

# print(certificates.get("Canada"))

# episodes = series.data['episodes']

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