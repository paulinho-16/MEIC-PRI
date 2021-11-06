from imdb import IMDb

# creating instance of IMDb
ia = IMDb()
 
# id
code = "6468322"

the_matrix = ia.get_movie(code)
 
# getting information
series = ia.get_movie(code)

# for i in series.data:
#     print(i)

print("TITLE: " + series['original title'])

print('Genres:')
for genre in series['genres']:
    print(genre)

cast = series['cast']

for person in cast:
    print(person['name'])

print("SEASONS: " + str(series['seasons']))

print('CERTIFICATES: ')
print(series['certificates']['Canada'])


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