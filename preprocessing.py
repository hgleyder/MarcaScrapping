# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from os import listdir
from os.path import isfile, join
from nltk.corpus import stopwords
import re
from nltk.stem import SnowballStemmer
stemmer = SnowballStemmer('spanish')

def getFilesFromPath(path):
    return [f for f in listdir(path) if isfile(join(path, f))]

def getPathFilesContent(path):
    fileNames = getFilesFromPath(path)
    filesAbsolutePath = []
    for name in fileNames:
        filesAbsolutePath.append(path + '/' + name)
    # get content from files
    contents = []
    for file_path in filesAbsolutePath:
        f = open(file_path, 'r+')
        aux = f.readlines()
        content = ""
        for line in aux:
            content += line
        contents.append(content)
    return contents


def removeStopWordsAndApplyStemmerFromContent(content):
    stopWords = set(stopwords.words('spanish'))

    words = re.sub("^\W|\d|[.!:@#$%^&*(){}_,;'+/*<>|~`\"\-?]", " ", content.lower()).split()
    wordsFiltered = []

    for w in words:
        if w not in stopWords:
            wordsFiltered.append(stemmer.stem(w.decode('utf-8')))

    return wordsFiltered


def getContentPerClass(clase):
    contents = getPathFilesContent('news/'+clase)
    instances = []
    for content in contents:
        # remover stopwords y aplicar stemming
        try:
            words = removeStopWordsAndApplyStemmerFromContent(content)
            instances.append(words)
        except:
            print ""
    return instances


def getNewsContentPositivasNegativas():
    clases = ['positivo', 'negativo']
    todosLosArticulos = {}
    for clase in clases:
        articulos = getContentPerClass(clase)
        todosLosArticulos[clase] = articulos
    return todosLosArticulos

def generarAtributosPositivasNegativas(instancias):
    instancias = getNewsContentPositivasNegativas()
    clases = ['positivo', 'negativo']
    wordsList = {}
    for clase in clases:
        for instance in instancias[clase]:
            wordsAdded = []
            for word in instance:
                if not word in wordsAdded:
                    wordsAdded.append(word)
                    if not word in wordsList:
                        wordsList[word] = 1
                    else:
                        wordsList[word] += 1
    return wordsList


def generateDatasetPositivasNegativas():
    articulos = getNewsContentPositivasNegativas()
    atributos = generarAtributosPositivasNegativas(articulos)
    for clase in articulos:
        for articulo in articulos[clase]:
            instancia = ''
            for key in atributos.iterkeys():
                instancia += str(articulo.count(key)) + ','
            instancia+=clase+"\n"
            f = open('datasets/dataset.csv', 'a+')
            f.write(instancia)
    print "Dataset creado de forma exitosa!"




generateDatasetPositivasNegativas()
