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

def tecnicasUsadas(catalogo,artistName):
    return controller.tecnicasUsadas(catalogo,artistName)

def hallarNacionalidades(catalogo):
    return controller.hallarNacionalidades(catalogo)

def nuevaExposicion(catalogo,fechaInicio,fechaFin):
    return controller.nuevaExposicion(catalogo,fechaInicio,fechaFin)

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
            fallece="Desconocida o aún vive"
        if genero=="":
            genero="No reporta"
        if nacionalidad=="":
            nacionalidad="Desconocida"
        print("Nombre: "+nombre+"\nGenero: "+genero+"\nFecha de nacimiento: "+nacido+"\nNacionalidad: "+nacionalidad+"\nFecha de fallemiento: "+fallece+"\n_______________________________\n")

def printArtworksResults(sortedArtworks,catalogo):
    ids=idOfArtist(catalogo)
    compradas=0
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
        nombresArtista=[]
        idArtistasActual=obra["ConstituentID"].replace("["," ").replace("]"," ").replace(","," ,").split(",")
        q=0
        while q!=len(idArtistasActual):
            g=1
            while g!=lt.size(ids):
                iD=lt.getElement(ids,g)[0]
                name=lt.getElement(ids,g)[1]
                if iD == idArtistasActual[q]:
                    nombresArtista.append(name)
                    nombres = ", ".join(nombresArtista)
                g+=1
            q+=1
        titulo,fecha,medio,dimensiones=obra["Title"],obra["Date"],obra["Medium"],obra["Dimensions"]
        if fecha=="":
            fecha="No se conoce la fecha de creación"
        if medio=="":
            medio="No se conoce el medio"
        if dimensiones=="":
            dimensiones="No se conocen las dimensiones de la obras"
        print("Titulo: "+titulo+"\nArtistas: "+nombres+"\nFecha: "+fecha+"\nMedio: "+medio+"\nDimensiones: "+dimensiones+"\n_______________________________\n")

def printMediumArtworks(catalogo):
    i=0
    while i!=lt.size(catalogo):
        titulo=lt.getElement(catalogo,i)['Title']
        fecha=lt.getElement(catalogo,i)['Date']
        medio=lt.getElement(catalogo,i)['Medium']
        dimensiones=lt.getElement(catalogo,i)['Dimensions']
        print('Titulo: '+titulo+'\nFecha: '+fecha+'\nMedio: '+medio+'\nDimensiones.: '+dimensiones+"\n_______________________________\n")
        i+=1

def printTop10Natonalitys(catalogo):
    i=1
    while i!=lt.size(catalogo)+1:
        nacionalidad=lt.getElement(catalogo,i)[0]
        numero=lt.getElement(catalogo,i)[1]
        print(nacionalidad+': '+str(numero)+'\n')
        i+=1



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
        nombreArtist=input("Ingrese el nombre del artista a consultar:\n")
        obrasArtista=tecnicasUsadas(catalogo,nombreArtist)
        print ("\nEl numero de obras realizadas por este artista son "+str(lt.size(obrasArtista[0]))+"\n")
        if lt.size(obrasArtista[0])!=0:
            print('El numero de tecnicas usadas por este artista son '+str(len(obrasArtista[1]))+'\n')
            print('La tecnica mas usada por este autor es '+str(obrasArtista[2])+' con '+str(lt.size(obrasArtista[3]))+' obra(s)\n')
            print('Las obras que usan dicha tecnica son: '+'\n_______________________________\n')
            printMediumArtworks(obrasArtista[3])
    elif int(inputs[0])==5:
        nacion=hallarNacionalidades(catalogo)
        print('\nEl TOP 10 nacionalidades por numero de obras es:\n')
        printTop10Natonalitys(nacion)
    elif int(inputs[0])==6:
        ids=controller.obrasMasNacionalidad(catalogo)
        print("los ids son: \n", ids )
    elif int(inputs[0])==7:
        print('Ordenando obras por fecha...') 
        obrasByDate=controller.sortArtworksByDate(catalogo)
        fechaInicio=int(input('Ingrese el anio inicial del rango:\n'))
        fechaFin=int(input('Ingrese el anio final del rango:\n'))
        obrasRango=nuevaExposicion(obrasByDate,fechaInicio,fechaFin)
        print ('\nEl numero de obras creadas en ese rango de fechas son '+str(lt.size(obrasRango))+'\n') 
    else:
        sys.exit(0)
sys.exit(0)


#preguntas pal profe
'''
-Cuantas de las medidas debemos tener en cuenta para calcular el precio? todas las medidas que tenga? 
o calcular lo que se pueda y sumarle la tarifa basica por los valores vacios?
- cual es la diferencia entre el largo y la profundidad de la obra? con cual deberiamos evaluar?
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