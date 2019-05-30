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

MIN_COUNT_ATTR = 10;

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

    for w in list(range(0, len(words))):
        # Tomando en cuenta negaciones
        if words[w] in ['ni', 'no', 'jamás']:
            wordsFiltered.append(words[w] + '-' + stemmer.stem(words[w+1].decode('utf-8')))

        elif words[w] not in stopWords:
            wordsFiltered.append(stemmer.stem(words[w].decode('utf-8')))

        # Bigramas
        if words[w] not in stopWords and w < len(words) - 1 and words[w+ 1] not in stopWords:

            wordsFiltered.append(stemmer.stem(words[w].decode('utf-8')) + '-' + stemmer.stem(words[w+1].decode('utf-8')))

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
            print("")
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
    f = open('datasets/dataset.csv', 'w+')
    f = open('datasets/classes.txt', 'w+')
    f = open('datasets/instances.txt', 'w+')
    f = open('datasets/attributes.txt', 'w+')
    attrSaved = False
    articulos = getNewsContentPositivasNegativas()
    atributos = generarAtributosPositivasNegativas(articulos)
    for clase in articulos:
        for articulo in articulos[clase]:
            instancia = ''
            filteredAttrs = (x for x in atributos.iterkeys() if atributos[x] >= MIN_COUNT_ATTR)
            for key in filteredAttrs:
                if not attrSaved:
                    f = open('datasets/attributes.txt', 'a+')
                    f.write(key+'\n')
                instancia += str(articulo.count(key)) + ','
            attrSaved = True
            f = open('datasets/instances.txt', 'a+')
            f.write(instancia[:-1]+'\n')
            f = open('datasets/classes.txt', 'a+')
            f.write(clase+'\n')

            instancia+=clase+"\n"
            f = open('datasets/dataset.csv', 'a+')
            f.write(instancia)
    print("Dataset creado de forma exitosa!")


def crearInstanciaConAtributos(words):
    f = open('datasets/attributes.txt', 'r+')
    atributos = f.readlines()
    aux = []
    for a in atributos:
        aux.append(a.replace('\n',""))
    atributos = aux

    instancia = []
    for palabra in atributos:
        cnt = words.count(palabra)
        instancia.append(cnt)

    return instancia


#
#
#
#
# generateDatasetPositivasNegativas()
