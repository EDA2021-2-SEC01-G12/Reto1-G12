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
    print("2- Listar cronológicamente obras adquiridas por el museo")
    print("3- Listar artistas nacidos en un rango de años específico")
    print("4- Clasificar obras de un artista por tecnica")
    print("5- Clasificar obras por la nacionalidad de sus autores")
    print("6- Calcular costo para transportar obras de un departamento del museo")
    print("7- Proponer nueva exposicion")
    print("0- Salir")

def initCatalog(type):
    return controller.initCatalog(type)


def sortArtworks(catalog, muestra, tipo):
    sorted=controller.sortArtworks(catalog,int(muestra),tipo)
    return sorted

def sortArtists(catalogo,fechaInicio,fechaFin):
    sorted=controller.sortArtists(catalogo,fechaInicio,fechaFin)
    return sorted
    
'''def printSortResults(sorted_artworks, sample=10): 
    size = lt.size(sorted_artworks) 
    if size > sample: 
        print("Las primeros ", sample, " obras ordenadas por su fecha de adquisición son:") 
        i=1 
        while i <= sample: 
            artwork = lt.getElement(sorted_artworks,i) 
            print('ID: ' + artwork["ConstituentID"] + ' Fecha: ' + 
                    artwork['DateAcquired'] ) 
            i+=1'''
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Elija el tipo de estructura en la cual se alamacenarán los datos: \n1. Array List\n2. Single Linked")
        type=input("")
        finish=True
        while finish:
            if type =="1":
                catalog=initCatalog("ARRAY_LIST")
                finish=False
            elif type=="2":
                catalog=initCatalog("SINGLE_LINKED")
                finish=False
            else:
                print(type+" no es una opción válida.\nSeleccione una opción válida")
                type=input("")
        print("Cargando información de los archivos ....")
        controller.addAuthors(catalog)
        controller.addArtworks(catalog)
        print("Los datos fueron cargados")
    elif int(inputs[0]) == 2:
        muestra=print("Ingrese el tamaño de la muestra de las obras de arte a ser ordenadas:")
        muestra1=int(input(""))
        terminado=True
        while terminado:
            if muestra1> int(lt.size(catalog["obras"])):
                print("El número ingresado supera el número de datos cargados, por favor ingrese un numero válido: ")
                muestra1=int(input(""))
            else:
                terminado=False
        sortType=input("Seleccione el algoritmo de ordenamiento para los datos:\n1. Insertion Sort.\n2. Merge Sort.\n3. Quick Sort.\n4. Shell Sort.\n")
        sort=sortArtworks(catalog,muestra1,sortType)
        tiempo=sort[0]
        print("El tiempo tardado en ordenar ",muestra1," elementos fue de ",tiempo," msg")
        newList=sort[1]
        print(newList)
    elif int(inputs[0]) ==3:
        añoInicial=int(input("Ingrese el año inicial del rango: "))
        añoFinal=int(input("Ingrese el año final del rango: "))
    else:
        sys.exit(0)
sys.exit(0)
