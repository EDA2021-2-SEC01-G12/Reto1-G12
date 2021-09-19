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


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import mergesort as ms
from DISClib.Algorithms.Sorting import quicksort as qs
import time 
assert cf

def newCatalog(type):
    catalog = {'artistas': None,
               'obras': None}

    catalog['artistas'] = lt.newList(type)
    catalog['obras'] = lt.newList(type,cmpfunction=cmpArtworkByDateAcquired)
    return catalog


"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

# Funciones para agregar informacion al catalogo

def addAuthors(catalog, author):
    lt.addLast(catalog["artistas"],author)

def addArtworks (catalog,artwork):
    lt.addLast(catalog["obras"],artwork)

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

def cmpArtworkByDateAcquired(artwork1, artwork2):
    art1=(artwork1["DateAcquired"]).split("-")
    art2=(artwork2["DateAcquired"]).split("-")
    if int(art1[0]) < int(art2[0]):
        return 1
    elif int(art1[0]) == int(art2[0]):
        if int(art1[1])<int(art2[1]):
            return 1
        elif int(art1[1])>int(art2[1]):
            return -1
        elif int(art1[1]) == int(art2[1]):
            if int(art1[2])<int(art2[2]):
                return 1
            elif int(art1[2]) == int(art2[2]):
                return 0
            else:
                return -1
    else:
        return -1

# Funciones de ordenamiento

def sortArtworks(catalogo,muestra, tipo):
    new=lt.subList(catalogo["obras"],1,muestra)
    new=new.copy()
    start_time = time.process_time()
    sorted =tipo.sort(new,cmpArtworkByDateAcquired)
    stop_time= time.process_time()
    timeSort= (stop_time-start_time)*1000
    return timeSort,sorted