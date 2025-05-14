import urllib.request, urllib.parse, urllib.error
import ssl
from bs4 import BeautifulSoup
import json

url = "https://www.imdb.com/title/tt6084202/"
headers = {
        'User-Agent': 'BeautifulSoupApp'
}

req = urllib.request.Request(url, headers=headers)
html = urllib.request.urlopen(req, context=ssl.create_default_context()).read()
soup = BeautifulSoup(html, 'html.parser')

# Extracts structured metadata (like title, director, cast) from the JSON-LD script block 
# used by IMDb for SEO and data indexing (type='application/ld+json' is standard for linked data)
data = json.loads(soup.find('script', type='application/ld+json').string)

print("Director(s):", [d['name'] for d in data.get('director', [])])
print("Writer(s):", [w['name'] for w in data.get('creator', []) if w['@type'] == 'Person'])
print("Stars:", [a['name'] for a in data.get('actor', [])])

awards_section = soup.find('li', attrs={'data-testid': 'award_information'})
if awards_section:
    awards_text = awards_section.find('span', class_='ipc-metadata-list-item__list-content-item')
    if awards_text:
        print("\nAwards:", awards_text.get_text())
    else:
        print("\nNo award info")
else:
    print("\nNo award info")

# Top cast
print("\nTop Cast:")
cast_items = soup.find_all('div', attrs={'data-testid': 'title-cast-item'})
if cast_items:
    index = 1
    for item in cast_items:
        actor = item.find('a', attrs={'data-testid': 'title-cast-item__actor'}) 
        role = item.find('a', attrs={'data-testid': 'cast-item-characters-link'})

        if actor:
            actor_name = actor.get_text()
            role_name = role.get_text() if role else ""
            if role_name:
                print(f"{index}. {actor_name} as {role_name}")
            else:
                print(f"{index}. {actor_name}")
            index += 1
else:
    print("Top cast not found.")
