# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def SepararPalabrasMinusculasDeArchivo(filePath, list=[]):
    f = open(filePath, "r")
    lines = f.readlines()
    lista = list

    for line in lines:
        aux = line.lower().replace("\n", "")
        for palabra in aux.split(" "):
            if not palabra in lista:
                lista.append(palabra)
    return lista

def CreateNamesList():
    archivosNombres = ["jugadoresSoccer.txt", "estadiosEquipos.txt"]
    listaDeNombres = []
    for file in archivosNombres:
        listaDeNombres = SepararPalabrasMinusculasDeArchivo(file, listaDeNombres)
    return listaDeNombres

print CreateNamesList()