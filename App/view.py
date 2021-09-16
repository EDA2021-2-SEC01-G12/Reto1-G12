"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listar cronologicamente los artistas")
    print("3- Listar cronologicamente las adquisiciones")
    print("4- Clasificar obras de un artista por tecnica")
    print("5- Clasificar las obras por la nacionalidad de sus creadores")
    print("6- Costo para transportar obras de un departamento")
    print("7- Proponer nueva exposicion")
    print("0- Salir")

def initCatalog(type):
    return controller.initCatalog(type)
    
def printSortResults(sorted_artworks, sample=10): 
    size = lt.size(sorted_artworks) 
    if size > sample: 
        print("Las primeros ", sample, " obras ordenadas por su fecha de adquisición son:") 
        i=1 
        while i <= sample: 
            artwork = lt.getElement(sorted_artworks,i) 
            print('ID: ' + artwork["ConstituentID"] + ' Fecha: ' + 
                    artwork['DateAcquired'] ) 
            i+=1
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Elija el tipo de estructura en la cual se alamacenarán los datos: \n1. Array List\n2. Single Linked")
        type=input("")
        if type =="1":
            catalog=initCatalog("ARRAY_LIST")
        else:
            catalog=initCatalog("SINGLE_LINKED")
        print("Cargando información de los archivos ....")
        controller.addAuthors(catalog)
        controller.addArtworks(catalog)
    elif int(inputs[0]) == 2:
        muestra=input("Ingrese el tamaño de la muestra de las obras de arte a ser ordenadas: ")
        sorted=controller.sortArtworks(catalog,int(muestra))
        printSortResults(sorted)
    else:
        sys.exit(0)
sys.exit(0)
