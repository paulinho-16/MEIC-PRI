import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/title/tt1190634/"

r = requests.get(url=url)
# create a BeautifulSoup object
soup = BeautifulSoup(r.text, 'html.parser')

# data = {}

# #page title
# title = soup.find('title')
# print(title.string)
# data["title"] = title.string

rating = soup.find("span", class_ = "AggregateRatingButton__RatingScore-sc-1ll29m0-1 iTLWoV").text
print(rating)

date = soup.find("span", class_ = "TitleBlockMetaData__ListItemText-sc-12ein40-2 jedhex").text
print(date)

print("Ep")

episodes = soup.find("span", "EpisodeNavigationForSeries__EpisodeCountSpan-sc-1aswzzz-3 jbsbnI")
print(episodes)

resume = soup.find("div", class_ = "ipc-html-content ipc-html-content--base").text
print(resume)

origin = soup.find("a", class_ = "ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link").text
print(origin)

def getMovieDetails(url):
    data = {}
    r = requests.get(url=url)
    # Create a BeautifulSoup object
    soup = BeautifulSoup(r.text, 'html.parser')

    #page title
    title = soup.find('title')
    data["title"] = title.string

    # rating
    ratingValue = soup.find("span", {"itemprop" : "ratingValue"})
    data["ratingValue"] = ratingValue.string

    # no of rating given
    ratingCount = soup.find("span", {"itemprop" : "ratingCount"})
    data["ratingCount"] = ratingCount.string

    # name
    titleName = soup.find("div",{'class':'titleBar'}).find("h1")
    data["name"] = titleName.contents[0].replace(u'\xa0', u'')

    # additional details
    subtext = soup.find("div",{'class':'subtext'})
    data["subtext"] = ""
    for i in subtext.contents:
        data["subtext"] += i.string.strip()

    # summary
    summary_text = soup.find("div",{'class':'summary_text'})
    data["summary_text"] = summary_text.string.strip()

    credit_summary_item = soup.find_all("div",{'class':'credit_summary_item'})
    data["credits"] = {}
    for i in credit_summary_item:
        item = i.find("h4")
        names = i.find_all("a")
        data["credits"][item.string] = []
        for i in names:
            data["credits"][item.string].append({
                "link": i["href"],
                "name": i.string
            })
    return data

# data = {}

# r = requests.get(url=boys_url)
# # create a BeautifulSoup object
# soup = BeautifulSoup(r.text, 'html.parser')

#page title
#title = soup.find('TitleHeader__TitleText-sc-1wu6n3d-0 cLNRlG')
# title = soup.find("div",{'class':'titleBar'})
# print(title)
# print(title.string)
# data["title"] = title.string


# rating
# ratingValue = soup.find("span", class_ = "AggregateRatingButton__RatingScore-sc-1ll29m0-1 iTLWoV")
# print(ratingValue)
# data["ratingValue"] = ratingValue.string
# print(data["ratingValue"])



