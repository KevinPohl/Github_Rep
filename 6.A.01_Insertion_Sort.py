#-----------------------------------------------------
# Filename: 6.A.01.py
# Version: 1.0
# Function: Assignment 01 from chapter 6
# Author: Kevin Pohl
# Last Change: 03.07.23
#-----------------------------------------------------

# Recherchiere die Funktionsweise des Insertion-Sort-Algorithmus! Nutze deine Kenntnisse über Funktionen, Schleifen und
# Kontrollstrukturen, um den Insertion Sort in Python zu implementieren!

#-----------------------------------------------------

# def insSort(liste:list):
#     startListe=liste
#     ergebnisListe=[]
#     einzelschritte=0 # print Zwischenschritte ja/nein
#     while len(startListe):
#         if len(ergebnisListe)==0:
#             ergebnisListe.append(startListe.pop(0))
#             if einzelschritte:print("Append 1st: ",ergebnisListe,startListe)
#         elif startListe[0]>ergebnisListe[-1]:
#             ergebnisListe.append(startListe.pop(0))
#             if einzelschritte:print("Append End: ",ergebnisListe,startListe)
#         else:
#             for i in range(len(ergebnisListe)):
#                 if startListe[0]<=ergebnisListe[i]:
#                     ergebnisListe.insert(i,startListe.pop(0))
#                     if einzelschritte:print("Insert:     ",ergebnisListe,startListe)
#     return ergebnisListe


def insSort(array):                           #function aus Lösung -> analysieren
    for i in range(1,len(array)):
        key_element = array[i]
        j=i-1
        while j>=0 and key_element<array[j]:
            array[j+1] = array[j]
            j=j-1
        array[j+1]=key_element




testliste=[5,4,8,0,6,1,2,9,7,7]
insSort(testliste)
print(testliste)
# insSort(testliste)


