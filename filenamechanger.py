#-----------------------------------------------------
# Filename: filenamechanger.py
# Version: 1.0
# Function: module change filenames in a folder
# Author: Kevin Pohl
# Last Change: 14.07.23
#-----------------------------------------------------


from tkinter.filedialog import askdirectory
from os import listdir,rename,walk,getcwd
# pfad = askdirectory(initialdir=getcwd())    # pfadauswahl
pfad="E:/Program Files/Python/Python311/MyScripts_kpo"
list=list(listdir(pfad))
# print(list)

# l1,l2,l3=[],[],[]
for i in range(len(list)):
    l1,l2,l3=next(walk(pfad))   # l1: 1 string Ordner +"/"+ l3 dateinamen (hier irr. l2 unterordner)
   
dateiauswahl=[i for i in l3 if ".py" in i] # alle .py dateien
alt_neu=[]
for i in dateiauswahl:
    nameneu=str(i[:-3]) # Alle .py entfernen
    nameneu=nameneu.replace("Ä","AE").replace("Ö","OE").replace("Ü","UE").replace("ä","ae")\
        .replace("ö","oe").replace("ü","ue").replace(".","_").replace("ß","ss").replace("","")     # alle unerwünschten Zeichen ändern
    nameneu=nameneu+".py"
    alt_neu.append((i,nameneu))

# rename()

for von,nach in alt_neu:
    von = l1+"/"+von
    nach = l1+"/"+nach
    # print(von)
    # print(nach)
    rename(src=von,dst=nach)



