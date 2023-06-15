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

import random

from PIL import Image
import requests
from io import BytesIO

# Choose randomized champion
random_champion = champions[random.randint(0, len(champions) - 1)]

# Create a formatted output
formatted_output = f"""
Randomly Chosen Champion:

Name: {random_champion['name']}
Image URL: {random_champion['image_url']}
"""

print(formatted_output)

from IPython.display import Image as DisplayImage

DisplayImage(url=random_champion['image_url'])
