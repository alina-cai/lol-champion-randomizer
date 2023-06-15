import random
import base64
import requests
from flask import Flask, render_template
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def random_champion():
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

    # Fetch the image and convert it to a base64-encoded data URI
    response = requests.get(random_champion['image_url'])
    image_data = base64.b64encode(response.content).decode('utf-8')
    image_data_uri = f"data:image/jpeg;base64,{image_data}"

    # Pass the additional information to the template
    return render_template('champion.html',
                           name=random_champion['name'],
                           image_url=image_data_uri,
                           release_date=random_champion['release_date'],
                           blue_essence=random_champion['blue_essence'],
                           rp=random_champion['rp'],
                           classs=random_champion['class'])

if __name__ == "__main__":
    app.run()