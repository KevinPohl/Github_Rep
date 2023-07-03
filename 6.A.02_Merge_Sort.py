#-----------------------------------------------------
# Filename: 6.A.02.py
# Version: 1.0
# Function: Assignment 2 from chapter 6
# Author: Kevin Pohl
# Last Change: 03.07.23
#-----------------------------------------------------

# Recherchiere die Funktionsweise des Merge-Sort-Algorithmus! Nutze deine Kenntnisse über Funktionen,
# Schleifen und Kontrollstrukturen, um den Merge Sort in Python zu implementieren!

#-----------------------------------------------------
def zufallsListe(listenlaenge:int):
    import random
    l1=[]
    for i in range(listenlaenge):
        l1.append(random.randint(1,1000))
    return l1
        
def mergeSorter(liste:list): # Listentrenner
    laenge=len(liste)
    if laenge>1:
        haelfte=laenge//2
        return merge(mergeSorter(liste[:haelfte]),mergeSorter(liste[haelfte:]))
    else:
        return liste
    
def merge(l1:list,l2:list=[]):
    rList=[]
    while len(l1)!=0 and len(l2)!=0:
        while l1[0]<=l2[0]:
            rList.append(l1.pop(0))
            break
        else:
            while l1[0]>l2[0]:
                rList.append(l2.pop(0))
                break
    else:
        while len(l1)!=0:
            rList.append(l1.pop(0))
        else:
            while len(l2)!=0:
                rList.append(l2.pop(0))
        return rList

zListe=zufallsListe(11)
print("unsortiert:",zListe)
print("MSsortiert:",mergeSorter(zListe))
