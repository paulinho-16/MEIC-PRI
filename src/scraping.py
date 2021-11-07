#https://bit.ly/2NyxdAG
from bs4 import BeautifulSoup
import requests
import re
import lxml.html
import sys

import pandas as pd

db = pd.read_csv('..\dataset\\netflix_list.csv', sep=",", low_memory=True)
# print(db)

def get_movie(id):
    url = 'http://www.imdb.com/title/' + id
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup)

    year = soup.

    # movies = soup.select('td.titleColumn')
    # links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
    # crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
    # ratings = [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name=ir]')]
    # votes = [b.attrs.get('data-value') for b in soup.select('td.ratingColumn strong')]

    # imdb = []

    # # Store each item into dictionary (data), then put those into a list (imdb)
    # for index in range(0, len(movies)):
    #     # Seperate movie into: 'place', 'title', 'year'
    #     movie_string = movies[index].get_text()
    #     movie = (' '.join(movie_string.split()).replace('.', ''))
    #     movie_title = movie[len(str(index))+1:-7]
    #     year = re.search('\((.*?)\)', movie_string).group(1)
    #     place = movie[:len(str(index))-(len(movie))]
    #     data = {"movie_title": movie_title,
    #             "year": year,
    #             "place": place,
    #             "star_cast": crew[index],
    #             "rating": ratings[index],
    #             "vote": votes[index],
    #             "link": links[index]}
    #     imdb.append(data)

    # for item in imdb:
    #     print(item['place'], '-', item['movie_title'], '('+item['year']+') -', 'Starring:', item['star_cast'])

get_movie('tt1488589')



# from requests import get
# url = 'https://www.imdb.com/title/tt1488589/'
# response = get(url)
# print(response.text[:250])


# url="https://www.imdb.com/search/title/?sort=num_votes,desc&start=1&title_type=feature&year=1950,2012"
# r = requests.get(url) 
# bs = BeautifulSoup(r.text)
# for movie in bs.findAll('td','title'):
#     title = movie.find('a').contents[0]
#     genres = movie.find('span','genre').findAll('a')
#     genres = [g.contents[0] for g in genres]
#     runtime = movie.find('span','runtime').contents[0]
#     rating = movie.find('span','value').contents[0]
#     year = movie.find('span','year_type').contents[0]
#     imdbID = movie.find('span','rating-cancel').a['href'].split('/')[2]
#     print (title, genres,runtime, rating, year, imdbID)





# -------------------------------------------------------------------------------------------------

#     print(requests.get("http://www.imdb.com/title/" + id))
#     hxs = lxml.html.document_fromstring(requests.get("http://www.imdb.com/title/" + id).content)
#     movie = {}
#     try:
#         print(hxs.xpath('//*[@id="overview-top"]/h1/span[1]'))
#         movie['title'] = hxs.xpath('//*[@id="overview-top"]/h1/span[1]/text()')[0].strip()
#     except IndexError:
#         movie['title'] = ""
#     try:
#         movie['year'] = hxs.xpath('//*[@id="overview-top"]/h1/span[2]/a/text()')[0].strip()
#     except IndexError:
#         try:
#             movie['year'] = hxs.xpath('//*[@id="overview-top"]/h1/span[3]/a/text()')[0].strip()
#         except IndexError:
#             movie['year'] = ""
#     try:
#         movie['certification'] = hxs.xpath('//*[@id="overview-top"]/div[2]/span[1]/@title')[0].strip()
#     except IndexError:
#         movie['certification'] = ""
#     try:
#         movie['running_time'] = hxs.xpath('//*[@id="overview-top"]/div[2]/time/text()')[0].strip()
#     except IndexError:
#         movie['running_time'] = ""
#     try:
#         movie['genre'] = hxs.xpath('//*[@id="overview-top"]/div[2]/a/span/text()')
#     except IndexError:
#         movie['genre'] = []
#     try:
#         movie['release_date'] = hxs.xpath('//*[@id="overview-top"]/div[2]/span[3]/a/text()')[0].strip()
#     except IndexError:
#         try:
#             movie['release_date'] = hxs.xpath('//*[@id="overview-top"]/div[2]/span[4]/a/text()')[0].strip()
#         except Exception:
#             movie['release_date'] = ""
#     try:
#         movie['rating'] = hxs.xpath('//*[@id="overview-top"]/div[3]/div[3]/strong/span/text()')[0]
#     except IndexError:
#         movie['rating'] = ""
#     try:
#         movie['metascore'] = hxs.xpath('//*[@id="overview-top"]/div[3]/div[3]/a[2]/text()')[0].strip().split('/')[0]
#     except IndexError:
#         movie['metascore'] = 0
#     try:
#         movie['description'] = hxs.xpath('//*[@id="overview-top"]/p[2]/text()')[0].strip()
#     except IndexError:
#         movie['description'] = ""
#     try:
#         movie['director'] = hxs.xpath('//*[@id="overview-top"]/div[4]/a/span/text()')[0].strip()
#     except IndexError:
#         movie['director'] = ""
#     try:
#         movie['stars'] = hxs.xpath('//*[@id="overview-top"]/div[6]/a/span/text()')
#     except IndexError:
#         movie['stars'] = ""
#     try:
#         movie['poster'] = hxs.xpath('//*[@id="img_primary"]/div/a/img/@src')[0]
#     except IndexError:
#         movie['poster'] = ""
#     try:
#         movie['gallery'] = hxs.xpath('//*[@id="combined-photos"]/div/a/img/@src')
#     except IndexError:
#         movie['gallery'] = ""
#     try:
#         movie['storyline'] = hxs.xpath('//*[@id="titleStoryLine"]/div[1]/p/text()')[0].strip()
#     except IndexError:
#         movie['storyline'] = ""
#     try:
#         movie['votes'] = hxs.xpath('//*[@id="overview-top"]/div[3]/div[3]/a[1]/span/text()')[0].strip()
#     except IndexError:
#         movie['votes'] = ""
#     return movie

# if __name__ == "__main__":
#     print(main(sys.argv[1]))