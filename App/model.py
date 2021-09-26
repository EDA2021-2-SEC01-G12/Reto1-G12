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
        id=" "+id+" "
        dato=(id,nombre)
        lt.addLast(ids,dato)
        i+=1
    return ids

def findArtistInfo(catalogo,artistName):
    ids=idOfArtist(catalogo)
    cat=catalogo["obras"]
    obrasArtista=lt.newList("ARRAY_LIST")
    idParaBuscar=""
    i=0
    encontrado=True
    while i !=lt.size(ids) and encontrado:
        name=lt.getElement(ids,i)[1]
        iD=lt.getElement(ids,i)[0]
        if name==artistName:
            idParaBuscar=iD
            encontrado=False
        i+=1
    j=0
    while j!= lt.size(cat):
        obra=lt.getElement(cat,j)
        consId=obra["ConstituentID"].replace(" ","").replace("["," ").replace("]"," ").replace(","," , ").split(",")
        if idParaBuscar in consId:
            lt.addLast(obrasArtista,obra)
        j+=1
    return obrasArtista

def tecnicasUsadas(catalogo,artistName):
    obrasArtista=findArtistInfo(catalogo,artistName)
    tecnicas=None
    if lt.size(obrasArtista)!=0:
        obrasArtista=sortArtworksByMedium(obrasArtista)
        tecnicas=(contarTecnica(obrasArtista))[0]
        masUsado=(contarTecnica(obrasArtista))[1]
        k=0
        obrasTecnicaMasUsada=lt.newList('ARRAY_LIST')
        while k!=lt.size(obrasArtista):
            obraAct=lt.getElement(obrasArtista,k)
            if obraAct['Medium'].lower()==masUsado:
                lt.addLast(obrasTecnicaMasUsada,obraAct)
            k+=1
    else:
        masUsado=None
        obrasTecnicaMasUsada=None
    return obrasArtista,tecnicas, masUsado,obrasTecnicaMasUsada

def contarTecnica(obras):
    i=0
    tecnicas={}
    while i !=lt.size(obras):
        tecnicaactual=(lt.getElement(obras,i)['Medium']).lower()
        if tecnicaactual not in tecnicas:
            tecnicas[tecnicaactual]=1
        else:
            tecnicas[tecnicaactual]+=1
        i+=1
    mayor=0
    nameMayor=None
    for j in tecnicas:
        if tecnicas[j]>mayor:
            mayor=tecnicas[j] 
            nameMayor= j    
    return tecnicas,nameMayor

def hallarNacionalidades(catalogo):
    nacion={}
    cat=sortArtistByNationality(catalogo['artistas'])
    i=0
    while i!=lt.size(cat):
        nacActual=lt.getElement(cat,i)['Nationality']
        if nacActual=="":
            nacActual="Desconocida"
        nomActual=(lt.getElement(cat,i)['DisplayName']).split(',')
        obrasActual=findArtistInfo(catalogo,nomActual[0])
        numObrasArtistActual=lt.size(obrasActual)
        if nacActual not in nacion:
            nacion[nacActual]=numObrasArtistActual
        else:
            nacion[nacActual]+=numObrasArtistActual
        i+=1
    nacionalidadesOrdenadas=lt.newList(datastructure='ARRAY_LIST')
    for k in nacion:
        nation=k
        numeroNation=nacion[k]
        dato=(nation,numeroNation)
        lt.addLast(nacionalidadesOrdenadas,dato)
    nacionalidadesOrdenadas=sortNationalityByNumber(nacionalidadesOrdenadas)
    nacionalidadesOrdenadas=lt.subList(nacionalidadesOrdenadas,1,10)
    return nacionalidadesOrdenadas

def nuevaExposicion(cat,fechaInicio,fechaFin):
    i=1
    contador=0
    primera=None
    ultimo=True
    while i!=lt.size(cat) and ultimo:
        dateActual=lt.getElement(cat,i)['Date']
        if dateActual=='':
            dateActual='0'
        if fechaInicio<=int(dateActual) and int(dateActual)<=fechaFin:
            contador+=1
        if int(dateActual)>=fechaInicio and primera==None:
            primera=i
        if int(dateActual)>fechaFin:
            ultimo=False
        i+=1
    obrasRangoFecha=lt.subList(cat,primera,contador)
    return obrasRangoFecha

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

def cmpArtworkByMedium(art1,art2):
    if art1["Medium"] < art2["Medium"]:
        return True
    else:
        return False

def cmpArtistByNationality(artist1,artist2):
    art1=artist1['Nationality']
    art2=artist2['Nationality']   
    if art1>art2:
        return True
    else:
        return False

def cmpArtistByNationalityNumber(nat1,nat2):
    if nat1[1]>nat2[1]:
        return True
    else:
        return False

def cmpArtworkByDate(art1,art2):
    if art1['Date']<art2['Date']:
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

def sortArtworksByMedium(catalogo):
    obrasOrdenadas=ms.sort(catalogo,cmpArtworkByMedium)
    return obrasOrdenadas

def sortArtistByNationality(catalogo):
    artistsNationality=ms.sort(catalogo,cmpArtistByNationality)
    return artistsNationality

def sortNationalityByNumber(catalogo):
    return ms.sort(catalogo,cmpArtistByNationalityNumber)

def sortArtworksByDate(catalogo):
    cat=catalogo['obras']
    obrasOrdenadas=ms.sort(cat,cmpArtworkByDate)
    return obrasOrdenadas









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

'''i=0
    tecnicas=lt.newList('ARRAY_LIST')
    while i !=lt.size(obras):
        tecnicaactual=(lt.getElement(obras,i)['Medium']).lower()
        if lt.isPresent(tecnicas,tecnicaactual)==0:
            lt.addLast(tecnicas,tecnicaactual)
        i+=1
    return tecnicas'''