import random

lista=[]

def veletlen():
    for i in range(0,10,1):

        szam=random.randint(5,15)

        lista.append(szam)

    return lista




def megszamlalas(lista):
    szamlalo = 0
    for i in lista:
        if i < 15:
            szamlalo += 1
    print(szamlalo)

def osszegzes():
    osszeg = 0

    for i in range (len(lista)): 

        osszeg += lista[i]  

    print(f"összeg: {osszeg}")

def minimum(lista):
    m = 0
    for i in range(1, len(lista)):  
        if m > lista[i]: 
            m = lista[i]  
    return m


def maximum(lista):
    m = 0
    for i in range(1, len(lista)):
        if m < lista[i]:
            m = lista[i]
    return m

def eldontes_tetel(): # vn e 13 and !(lista[i] == 13)  i<n ////// mind > 10  and (lista[i] == 13)   i>= n:
    lista = [13, 14, 18, 20, 1, 2, 3, 4, 5]
    i = 0
    while (i < len(lista)) and not (lista[i] == 13):  
        i += 1

    return (i < len(lista)) 

 
def linearis_kereses():   # hol van a 15, ha van benne?

    lista = [11, 1, 18, 20, 15, 2, 3, 4]
    i = 0
    while i < len(lista):
        if lista[i] == 15: 
            return i+1 
        i += 1
    return -1
