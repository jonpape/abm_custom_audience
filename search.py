import requests
from googlesearch import search
from bs4 import BeautifulSoup

query = 'OpenAI'
related_searches = []

for url in search(query, num_results=0):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    related_search_tags = soup.select('div[id="brs"] a')
    for tag in related_search_tags:
        related_searches.append(tag.text)

print(related_searches)
