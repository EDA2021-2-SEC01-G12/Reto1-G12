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
    posArtista=None
    contador=0
    i=1
    segundo=True
    while i!= lt.size(catalogo) and segundo:
        if fecha1<= int(lt.getElement(catalogo,i)["BeginDate"]) <=fecha2:
            contador+=1
        if ((int(lt.getElement(catalogo,i)["BeginDate"]))==fecha1) and posArtista==None:
            posArtista=lt.isPresent(catalogo,(lt.getElement(catalogo,i)))
        if (int(lt.getElement(catalogo,i)["BeginDate"]))==fecha2:
            contador+=1
            if (lt.getElement(catalogo,i+1)["BeginDate"])!=fecha2:
                segundo=False
        i+=1
    ltArtistasRango=lt.subList(catalogo,posArtista,contador)
    return ltArtistasRango


# Funciones utilizadas para comparar elementos dentro de una lista

def cmpArtworkByDateAcquired(artwork1, artwork2):
    if artwork1["DateAcquired"]!="":
        art1=(artwork1["DateAcquired"]).split("-")
    else:
        art1="0"
    if artwork2["DateAcquired"]!="":
        art2=(artwork2["DateAcquired"]).split("-")
    else:
        art2="0" 
    if int(art1[0]) < int(art2[0]):
        return True
    else:
        False

def cmpArtistByBirthDate(artista1,artista2):
    artista1=int(artista1["BeginDate"])
    artista2=int(artista2["BeginDate"])
    if artista1 < artista2:
        return True
    else:
        return False

    

# Funciones de ordenamiento    

def sortArtworks(catalogo,muestra, tipo):
    new=lt.subList(catalogo["obras"],1,muestra)
    new=new.copy()
    if tipo=="1":
        tipo=ins
    elif tipo=="2":
        tipo=ms
    elif tipo=="3":
        tipo=qs
    else:
        tipo=sa
    start_time = time.process_time()
    sorted =tipo.sort(new,cmpArtworkByDateAcquired)
    stop_time= time.process_time()
    timeSort= (stop_time-start_time)*1000
    return timeSort,sorted

def sortArtists(catalogo):
    artistasOrdenados=ms.sort(catalogo["artistas"],cmpArtistByBirthDate)
    return artistasOrdenados