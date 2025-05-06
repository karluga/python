# To run this, download the BeautifulSoup zip file
# from ViA Moodle this study course page
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = "https://www.w3schools.com/"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/120.0'})
html = urllib.request.urlopen(req).read()

soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
