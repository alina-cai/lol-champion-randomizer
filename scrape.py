import urllib3
from bs4 import BeautifulSoup

# Get html
http = urllib3.PoolManager()
r = http.request('GET', "https://leagueoflegends.fandom.com/wiki/List_of_champions")

# Initialize Beautiful Soup
soup = BeautifulSoup(r.data, 'html.parser')

# Scrape relevant data
champions = []

tables = soup.find_all("table", {"class":"article-table"})
tbody = tables[0].find("tbody")
trs = tbody.find_all("tr")

for tr in trs[1:]:
    tds = tr.find_all("td")
    name = tds[0].get("data-sort-value")
    image_url = tds[0].find("img").get("data-src")
    # image = http.request('GET', image_url).data

    champions.append({
        "name": name,
        "image_url": image_url,
        # "image": image,
    })

import pprint
import random

# Choose randomized champion
pprint.pprint(champions[random.randint(0,len(champions)-1)])