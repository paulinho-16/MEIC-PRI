import pandas as pd
import numpy as np
import re
import lxml

from bs4 import BeautifulSoup
from requests import get

url= "https://www.imdb.com/title/tt1488589/"

page = get(url)
soup = BeautifulSoup(page.content, 'lxml')

content = soup.find(id="main")

print(soup)

articleTitle = soup.find("h1", class_="header").text.replace("\n","")

print(articleTitle)