# import both Requests and Beautifulsoup

import requests

from bs4 import BeautifulSoup

class IMDBScraper:
   def __init__(self, url):
       self.url = url
       self.download_page()

   def download_page(self):

       # method for downloading the hotel page

       self.page = requests.get(self.url).text

   def scrape_data(self):
       #method for scraping out movie title and description
       soup = BeautifulSoup(self.page, "html.parser")
       movie_title = soup.find("h1", {"data-testid": "hero-title-block__title"}).text
       movie_description = soup.find("span", {"data-testid": "plot-xl"}).text
       movie_year = soup.find("span", {"class": "TitleBlockMetaData__ListItemText-sc-12ein40-2 jedhex"}).text
       try:
          movie_rating = soup.find("span", {"class": "AggregateRatingButton__RatingScore-sc-1ll29m0-1 iTLWoV"}).text
       except:
          movie_rating = "NaN"

       try:
          movie_age = soup.find("span", {"class": "ipc-link ipc-link--baseAlt ipc-link--inherit-color TitleBlockMetaData__StyledTextLink-sc-12ein40-1 rgaOW"}).text
       except:
          movie_age = "NaN"
       
       try:
          movie_duration = soup.find("span", {"class": "ipc-inline-list__item"}).text
       except:
          movie_duration = "NaN"
       
       
       return {"title": movie_title,
               "description": movie_description,
               "year": movie_year,
               "rating": movie_rating,
               "age": movie_age,
               "duration": movie_duration
               }

urls = ["https://www.imdb.com/title/tt2382320","https://www.imdb.com/title/tt1488589"]

for url in urls:
   x = IMDBScraper(url)
   print(x.scrape_data())