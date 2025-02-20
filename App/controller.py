﻿"""
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
 """


import config as cf
import model
import csv






"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog

# Funciones para la carga de datos

def addAuthors(catalog):
    authorsFile= cf.data_dir + "Artists-utf8-large.csv" 
    autFile = csv.DictReader(open(authorsFile, encoding='utf-8'))
    for author in autFile:
        model.addAuthors(catalog,author)

def addArtworks (catalog):
    artworksFile = cf.data_dir + "Artworks-utf8-large.csv"
    art= csv.DictReader (open(artworksFile, encoding="utf-8"))
    for line in art:
        model.addArtworks(catalog,line)
    
# Funciones de ordenamiento

def sortArtworks(catalogo):
    return model.sortArtworks(catalogo)

def sortArtworksByDate(catalogo):
    return model.sortArtworksByDate(catalogo)

# Funciones de consulta sobre el catálogo

def artistasEnRango(catalogo,fecha1,fecha2):
    return model.artistasEnRango(catalogo,fecha1,fecha2)

def obrasPorDateAcquired(catalogo, fechaInicio, fechaFin):
    return model.obrasPorDateAcquired(catalogo, fechaInicio, fechaFin)

def idOfArtist (catalogo):
    return model.idOfArtist(catalogo)

def tecnicasUsadas(catalogo,artistName):
    return model.tecnicasUsadas(catalogo,artistName)

def hallarNacionalidades(catalogo):
    return model.hallarNacionalidades(catalogo)

def nuevaExposicion(catalogo,fechaInicio,fechaFin,areaDisponible):
    return model.nuevaExposicion(catalogo,fechaInicio,fechaFin,areaDisponible)

def obrasMasNacionalidad(catalogo):
    return model.obrasMasNacionalidad(catalogo)

def obrasPorDepartamento(catalogo,departamento):
    return model.obrasPorDepartamento(catalogo,departamento)