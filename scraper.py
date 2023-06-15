import requests
from bs4 import BeautifulSoup
import random

# Get html
r = requests.get("https://leagueoflegends.fandom.com/wiki/List_of_champions")

# Initialize Beautiful Soup
soup = BeautifulSoup(r.content, 'html.parser')

# Scrape relevant data
champions = []

tables = soup.find_all("table", {"class": "article-table"})
tbody = tables[0].find("tbody")
trs = tbody.find_all("tr")

for tr in trs[1:]:
    tds = tr.find_all("td")
    name = tds[0].get("data-sort-value")
    image_url = tds[0].find("img").get("data-src")
    release_date = tds[2].get_text(strip=True)
    blue_essence = tds[4].get_text(strip=True)
    rp = tds[5].get_text(strip=True)
    classs = tds[1].get_text(strip=False)

    champions.append({
        "name": name,
        "image_url": image_url,
        "release_date": release_date,
        "blue_essence": blue_essence,
        "rp": rp,
        "class": classs,
    })

# Choose randomized champion
random_champion = random.choice(champions)

# Create a formatted output
formatted_output = f"""
Randomly Chosen Champion:

Name: {random_champion['name']}
Image URL: {random_champion['image_url']}
Release Date: {random_champion['release_date']}
Blue Essence: {random_champion['blue_essence']}
RP: {random_champion['rp']}
Class: {random_champion['class']}
"""

print(formatted_output)