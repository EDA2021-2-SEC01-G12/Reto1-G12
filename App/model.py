"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 
 """


from DISClib.DataStructures.arraylist import getElement
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import mergesort as ms
from DISClib.Algorithms.Sorting import quicksort as qs
import time 
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    catalog = {'artistas': None,
               'obras': None}

    catalog['artistas'] = lt.newList(datastructure="ARRAY_LIST")
    catalog['obras'] = lt.newList(datastructure="ARRAY_LIST")
    return catalog

# Funciones para agregar informacion al catalogo

def addAuthors(catalog, author):
    lt.addLast(catalog["artistas"],author)

def addArtworks (catalog,artwork):
    lt.addLast(catalog["obras"],artwork)

# Funciones para creacion de datos

# Funciones de consulta

def artistasEnRango(catalogo,fecha1,fecha2):
    cat=sortArtists(catalogo)
    posArtista=None
    contador=0
    i=1
    segundo=True
    while i<= lt.size(cat) and segundo:
        if fecha1<= int((lt.getElement(cat,i))["BeginDate"]) and int((lt.getElement(cat,i))["BeginDate"])<=fecha2:
            contador+=1
        if ((int((lt.getElement(cat,i))["BeginDate"]))>=fecha1) and posArtista==None:
            posArtista=i
        if (int((lt.getElement(cat,i))["BeginDate"]))>fecha2:
            segundo=False
        i+=1
    ltArtistasRango=lt.subList(cat,posArtista,contador)
    return ltArtistasRango

def obrasPorDateAcquired(catalogo, fechaInicio:str, fechaFin:str):
    cat=catalogo
    fechaInicio=int(fechaInicio.replace("-","")) 
    fechaFin=int(fechaFin.replace("-",""))
    posObra=None
    contador=0
    i=1
    ultimo=True
    while i<=lt.size(cat) and ultimo:
        dateAcquired=(lt.getElement(cat,i)["DateAcquired"])
        if dateAcquired=="":
            dateAcquired="0-0-0"
        dateAcquired=int(dateAcquired.replace("-",""))
        if fechaInicio<= dateAcquired and dateAcquired<=fechaFin:
            contador+=1
        if (dateAcquired>=fechaInicio) and posObra==None:
            posObra=i
        if dateAcquired>fechaFin:
            segundo=False
        i+=1
    ltObrasSorted=lt.subList(cat,posObra,contador)
    return ltObrasSorted

def idOfArtist(catalogo):
    cat=catalogo["artistas"]
    ids=lt.newList("ARRAY_LIST")
    i=1
    while i !=lt.size(cat):
        nombre=(lt.getElement(cat,i)["DisplayName"]).split(",")
        nombre=nombre[0]
        id=lt.getElement(cat,i)["ConstituentID"]
        dato=(id,nombre)
        lt.addLast(ids,dato)
        i+=1
    return ids

# Funciones utilizadas para comparar elementos dentro de una lista

def cmpArtworkByDateAcquired(artwork1, artwork2):
    if artwork1["DateAcquired"]=="":
        art1="0-0-0"
        art1=art1.split("-")
    else:
        art1=(artwork1["DateAcquired"]).split("-")
    if artwork2["DateAcquired"]=="":
        art2="0-0-0"
        art2=art2.split("-")
    else:
        art2=(artwork2["DateAcquired"]).split("-")
    if int(art1[0]) < int(art2[0]):
        return True
    elif int(art1[0]) == int(art2[0]):
        if int(art1[1]) < int(art2[1]):
            return True
        elif int(art1[1]) == int(art2[1]):
            if int(art1[2]) < int(art2[2]):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def cmpArtistByBirthDate(artista1,artista2):
    artista1=int(artista1["BeginDate"])
    artista2=int(artista2["BeginDate"])
    if artista1 < artista2:
        return True
    else:
        return False

    

# Funciones de ordenamiento    

def sortArtworks(catalogo):
    cat=catalogo["obras"]
    obrasOrdenadas =ms.sort(cat,cmpArtworkByDateAcquired)
    return obrasOrdenadas

def sortArtists(catalogo):
    cat=catalogo["artistas"]
    artistasOrdenados=ms.sort(cat,cmpArtistByBirthDate)
    return artistasOrdenados




#codigo pa despues
'''def sortArtworks(catalogo):
    new=lt.subList(catalogo["obras"],1,muestra)
    new=new.copy()
    start_time = time.process_time()
    sorted =ms.sort(new,cmpArtworkByDateAcquired)
    stop_time= time.process_time()
    timeSort= (stop_time-start_time)*1000
    return timeSort,sorted'''



'''while i<=lt.size(cat) and ultimo:
        dateAcquired=(lt.getElement(cat,i)["DateAcquired"])
        if dateAcquired=="":
            dateAcquired="0-0-0"
        dateAcquired=dateAcquired.split("-")
        if int(fechaInicio[0])<= int(dateAcquired[0]):
            if int(fechaInicio[1])<= int(dateAcquired[1]) :
                if int(fechaInicio[2])<= int(dateAcquired[2]) :
                    if int(dateAcquired[0]) <= int(fechaFin[0]): 
                        if int(dateAcquired[1]) <= int(fechaFin[1]):
                            if int(dateAcquired[2]) <= int(fechaFin[2]):
                                contador +=1
        if ((int(dateAcquired[0])>=int(fechaInicio[0]))) and (int(dateAcquired[1])>=int(fechaInicio[1])) and ((int(dateAcquired[2])>=int(fechaInicio[2]))) and posObra==None: 
            posObra=i
        if int(dateAcquired[0]) > int(fechaFin[0]) and int(dateAcquired[1]) > int(fechaFin[1]) and int(dateAcquired[2]) > int(fechaFin[2]):
            ultimo=False
        i+=1'''