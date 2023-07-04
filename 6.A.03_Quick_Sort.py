#-----------------------------------------------------
# Filename: 6.A.02.py
# Version: 1.0
# Function: Assignment 2 from chapter 6
# Author: Kevin Pohl
# Last Change: 04.07.23
#-----------------------------------------------------

# Recherchiere die Funktionsweise des Quick-Sort-Algorithmus! Nutze deine Kenntnisse über
# Funktionen, Schleifen und Kontrollstrukturen, um den Quick Sort in Python zu implementieren!

#-----------------------------------------------------
def zufallsZahl(min:int,max:int):import random;return random.randint(min,max)
def zufallsListe(listenlaenge:int):
    l1=[]
    for i in range(listenlaenge):
        l1.append(zufallsZahl(1,1000))
    return l1

def quickSort(liste:list):
    if len(liste)<=1:
        return liste
    else:
        zZ=zufallsZahl(0,len(liste)-1) # Pivot wird rnd ausgewählt
        pivotWert=[0]
        pivotWert[0]=liste[zZ]
        if zZ==0:
            listenSplice=liste[1:]
        elif zZ==len(liste)-1:
            listenSplice=liste[:-1]
        else:
            listenSplice=liste[:zZ]+liste[zZ+1:]
        links=[x for x in listenSplice if x < pivotWert[0]]
        rechts=[y for y in listenSplice if y >= pivotWert[0]]
        # print("sortiert:",liste,"Piv:",pivotWert)
        # print(links,pivotWert,rechts,listenSplice)
        return quickSort(links)+pivotWert+quickSort(rechts)

zL=zufallsListe(20)
print(zL,quickSort(zL),sep='\n')






