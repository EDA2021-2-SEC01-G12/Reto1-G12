"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 * p
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
    print("2- Listar artistas nacidos en un rango de años específico")
    print("3- Listar cronológicamente obras adquiridas por el museo")
    print("4- Clasificar obras de un artista por tecnica")
    print("5- Clasificar obras por la nacionalidad de sus autores")
    print("6- Calcular costo para transportar obras de un departamento del museo")
    print("7- Proponer nueva exposicion")
    print("0- Salir")

def initCatalog():
    return controller.initCatalog()


def sortArtworks(catalog, muestra, tipo):
    sorted=controller.sortArtworks(catalog,int(muestra),tipo)
    return sorted

def artistasEnRango(catalogo,fecha1, fecha2):
    return controller.artistasEnRango(catalogo,fecha1,fecha2)

def printSortResults(sortedArtist): 
    i=1
    j=-4
    artistas=True
    print("Los primeros y últimos tres artistas dentro dentro de ese rango son: \n_______________________________\n")
    while artistas:
        if i!=4:
            artista=lt.getElement(sortedArtist,i)
            i+=1
        else:
            artista=lt.getElement(sortedArtist,j)
            j+=1
            if j==-1:
                artistas=False
        nombre,genero,nacionalidad,nacido,fallece=artista["DisplayName"],artista["Gender"],artista["Nationality"],artista["BeginDate"],artista["EndDate"]
        if nacido=="0":
            nacido="Desconocida"
        if fallece=="0":
            fallece="Desconocida"
        if genero=="":
            genero="No reporta"
        print("Nombre: "+nombre+"\nGenero: "+genero+"\nFecha de nacimiento: "+nacido+"\nNacionalidad: "+nacionalidad+"\nFecha de fallemiento: "+fallece+"\n_______________________________\n")
        
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        catalogo=initCatalog()
        print("Cargando información de los archivos ....")
        controller.addAuthors(catalogo)
        controller.addArtworks(catalogo)
        print("Los datos fueron cargados")
    elif int(inputs[0]) == 2:
        print("Ordenando artistas por fecha de nacimiento...\n")
        fechaInicial=int(input("Ingrese el año inicial del rango: "))
        fechaFinal=int(input("Ingrese el año final del rango: "))
        newList=artistasEnRango(catalogo,fechaInicial,fechaFinal)
        print("\nEntre ",fechaInicial," y ",fechaFinal," nacieron ",lt.size(newList),"artistas\n")
        printSortResults(newList)
    elif int(inputs[0]) ==3:
        pass
    else:
        sys.exit(0)
sys.exit(0)





#codigo pa despues


'''print("Elija el tipo de estructura en la cual se alamacenarán los datos: \n1. Array List\n2. Single Linked")
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
                type=input("")'''


'''muestra=print("Ingrese el tamaño de la muestra de las obras de arte a ser ordenadas:")
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
        newList=sort[1]
        tiempo=sort[0]
        print("El tiempo tardado en ordenar ",muestra1," elementos fue de ",tiempo," msg")'''