import requests
import pandas as pd
from bs4 import BeautifulSoup

""" headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

response = requests.get('https://www.imdb.com/title/tt0268093/episodes/?ref_=login', headers=headers) """

file_path = '/Users/rishabhbhartiya/Desktop/Ramayana- TV Series (1987-88)/index.html'

with open(file_path, 'r') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

episodes = soup.find("section", class_="sc-dd387b12-0 HZmZH")
print(episodes)

Ramayana_Episode = []

for episode in episodes:
    Episode_Number = episode.find("div",class_="ipc-title__text")
    Episode_Title = episode.find("div",class_="ipc-title__text")
    Aired_Date = episode.find("span",class_="sc-ccd6e31b-10 dYquTu")
    Epidode_Summary = episode.find("div",class_="ipc-html-content-inner-div")
    Rating = episode.find("span",class_="ipc-rating-star--rating")
    Ramayana_Episode.append({
        'EPISODE': Episode_Number.get_text(),
        'TITLE':Episode_Title.get_text(),
        'AIRED ON':Aired_Date,
        'SUMMARY':Epidode_Summary,
        'RATING':Rating.get_text()
    })

df = pd.DataFrame(Ramayana_Episode)
df.to_csv("RAMAYANA.csv")