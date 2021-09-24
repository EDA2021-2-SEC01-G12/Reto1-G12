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


def sortArtworks(catalog):
    sorted=controller.sortArtworks(catalog)
    return sorted

def artistasEnRango(catalogo,fecha1, fecha2):
    return controller.artistasEnRango(catalogo,fecha1,fecha2)

def obrasPorDateAcquired(catalogo, fechaInicio, fechaFin):
    return controller.obrasPorDateAcquired(catalogo, fechaInicio, fechaFin)

def idOfArtist(catalogo):
    return controller.idOfArtist(catalogo)

#Funciones para imprimir resultados

def printSortResults(sortedArtist): 
    i=1
    j=-4
    artistas=True
    print("Los primeros y últimos tres artistas dentro de ese rango son: \n_______________________________\n")
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

def printArtworksResults(sortedArtworks,catalogo):
    ids=idOfArtist(catalogo)
    compradas=0
    print(ids)
    z=1
    while z!=lt.size(sortedArtworks):
        credit=lt.getElement(sortedArtworks,z)["CreditLine"]
        if credit!="":
            if "purchase" in (str(credit)).lower():
                compradas+=1
        z+=1
    i=1
    j=-4
    obras=True
    print("El número de obras que fueron compradas por el museo son ",compradas)
    print("Las primeras y últimas tres obras dentro de ese rango son: \n_______________________________\n")
    while obras:
        if i!=4:
            obra=lt.getElement(sortedArtworks,i)
            i+=1
        else:
            obra=lt.getElement(sortedArtworks,j)
            j+=1
            if j==-1:
                obras=False
        nombresArtista=""
        idArtistasActual=obra["ConstituentID"].replace("[","").replace("]","").split(",")
        print(idArtistasActual)
        q=0
        while q!=lt.size(ids):
            iD=lt.getElement(ids,q)[0]
            name=lt.getElement(ids,q)[1]
            g=0
            while g!=len(idArtistasActual):
                if iD == idArtistasActual[g]:
                    nombresArtista+=name
                g+=1
            q+=1
        titulo,fecha,medio,dimensiones=obra["Title"],obra["Date"],obra["Medium"],obra["Dimensions"]
        if fecha=="":
            fecha="No se conoce la fecha de creación"
        if medio=="":
            medio="No se conoce el medio"
        if dimensiones=="":
            dimensiones="No se conocen las dimensiones de la obras"
        print("Titulo: "+titulo+"\nArtistas: "+nombresArtista+"\nFecha: "+fecha+"\nMedio: "+medio+"\nDimensiones: "+dimensiones+"\n_______________________________\n")






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
        print("Ordenando obras por fecha de adquisición..\n")
        listaOrdenada=sortArtworks(catalogo)
        anioInicio,mesInicio,diaInicio,anioFin,mesFin,diaFin=True,True,True,True,True,True
        print("Ingrese el año inicial en formato de 4 dígitos:")
        anio1=input("")
        while anioInicio:
            if len(anio1)!=4:
                print("El número ingresado tiene un formato invalido")
                anio1=input("")
            else:
                anioInicio=False
        print("Ingrese el mes inicial en formato de 2 dígitos:")
        mes1=input("")
        while mesInicio:
            if len(mes1)!=2:
                print("El número ingresado tiene un formato invalido")
                mes1=input("")
            else:
                mesInicio=False
        print("Ingrese el dia inicial en formato de 2 dígitos:")
        dia1=input("")
        while diaInicio:
            if len(dia1)!=2:
                print("El número ingresado tiene un formato invalido")
                dia1=input("")
            else:
                diaInicio=False
        print("Ingrese el año final en formato de 4 dígitos:")
        anio2=input("")
        while anioFin:
            if len(anio2)!=4:
                print("El número ingresado tiene un formato invalido")
                anio2=input("")
            else:
                anioFin=False
        print("Ingrese el mes final en formato de 2 dígitos:")
        mes2=input("")
        while mesFin:
            if len(mes2)!=2:
                print("El número ingresado tiene un formato invalido")
                mes2=input("")
            else:
                mesFin=False
        print("Ingrese el dia inicial en formato de 2 dígitos:")
        dia2=input("")
        while diaFin:
            if len(dia2)!=2:
                print("El número ingresado tiene un formato invalido")
                dia2=input("")
            else:
                diaFin=False
        fecha1=anio1+"-"+mes1+"-"+dia1
        fecha2=anio2+"-"+mes2+"-"+dia2
        obrasSorted=obrasPorDateAcquired(listaOrdenada,fecha1,fecha2)
        print("Entre "+fecha1+" y "+fecha2+" el museo adquirió ",lt.size(obrasSorted)," obras")
        printArtworksResults(obrasSorted,catalogo)
    elif int(inputs[0])==4:
        lista=idOfArtist(catalogo)
        print(lista)
    elif int(inputs[0])==5:
        pass
    elif int(inputs[0])==6:
        pass
    elif int(inputs[0])==7:
        pass
    else:
        sys.exit(0)
sys.exit(0)


#preguntas pal profe
'''
-A que se refiere con medio
-Existen datos incompletos? es decir datos solo con año
-Se puede usar un diccionario para hacer la relacion id-nombre?
'''



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


'''iD=lt.getElement(ids,q)[0]
            name=lt.getElement(ids,q)[1]
            if iD in idArtistasActual:
                idArtistasActual.replace(iD,name)
            q+=1
        print(q)
        print(idArtistasActual)'''