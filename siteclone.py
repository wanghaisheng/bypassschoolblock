import requests
import json
from bs4 import BeautifulSoup

page = requests.get('https://just-fall.github.io/category/new.html')
soup = BeautifulSoup(page.text, 'html.parser')

for x in soup.find_all('a'):
  gamepage = requests.get('https://just-fall.github.io/go'+x.get('href')[3:])
  game = BeautifulSoup(gamepage.text, 'html.parser')
  iframe = game.find('iframe')
  if iframe != None:
    with open('create/links', 'a') as links:
      links.write(iframe.get('src')+'\n')
    with open('create/names', 'a') as links:
      links.write(game.find('h1').text[:-10] + '\n')

for x in soup.find_all('img'):
  with open('create/thumbs', 'a') as thumbs:
    thumbs.write(x.get('src')+'\n')

