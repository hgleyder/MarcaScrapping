import requests
import json
from bs4 import BeautifulSoup

r = requests.get('https://newsapi.org/v2/everything?sources=marca&apiKey=96498205418644a0b5f619f9d99fc807')
datastore = json.loads(r.text)

# Cargar record
f = open("record.txt", "r")
record =  []
for line in f.readlines():
    record.append(line.replace('\n', ''))


# filtrar articulos en espanol unicamente
for article in datastore['articles']:
    if not 'marca.com/en/' in article['url'] and not article['publishedAt'] in record and not 'en directo' in article['title'].lower():
        # guardar en el record el articulo
        f = open("record.txt", "a+")
        f.write(article['publishedAt']+'\n')
        print(article['title'] + " ---> added")

        raw_html = requests.get(article['url']).content
        html = BeautifulSoup(raw_html, 'html.parser')
        text = article['title']+"\n"
        for section in  html.select('.cols-30-70 > p'):
            text += section.text + '\n'
        f = open("news/"+article['publishedAt']+".txt", "w+")
        f.write(text)