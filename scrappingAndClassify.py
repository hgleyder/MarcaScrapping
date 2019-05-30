# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import requests
import json
from bs4 import BeautifulSoup
from joblib import load
from firebase import firebase
from preprocessing import removeStopWordsAndApplyStemmerFromContent, crearInstanciaConAtributos
import numpy as np

firebase = firebase.FirebaseApplication('https://sentimarca.firebaseio.com/', None)
result = firebase.get('/news', None)

clf = load("model.o")

r = requests.get('https://newsapi.org/v2/everything?sources=marca&apiKey=96498205418644a0b5f619f9d99fc807')
datastore = json.loads(r.text)


for article in datastore['articles']:
    if not 'marca.com/en/' in article['url'] and not 'en directo' in article['title'].lower():
        raw_html = requests.get(article['url']).content
        html = BeautifulSoup(raw_html, 'html.parser')
        text = article['title']+"\n"
        content = ""
        for section in  html.select('.cols-30-70 > p'):
            text += section.text + '\n'
            content += section.text + '\n'

        # CLASIFICAR UTILIZANDO MODELO AQUI
        palabras = removeStopWordsAndApplyStemmerFromContent(text)
        instancia = crearInstanciaConAtributos(palabras)
        prediction = clf.predict(np.array([instancia]))

        classes = ['positivo', 'negativo']


        firebase.put('/news', article['publishedAt'],
                     { 'title': article['title'],
                       'publishedAt': article['publishedAt'],
                       'content': content,
                       'clasificacion': classes[prediction[0]],
                       'imageUrl': article['urlToImage'],
                       'url': article['url']
                    })
        print(article['title']+ " ---> clasificada: " + classes[prediction[0]])