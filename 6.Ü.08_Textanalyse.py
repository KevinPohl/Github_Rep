#-----------------------------------------------------
# Filename: 6.Ü.08.py
# Version: 1.0
# Function: Exercise 8 from chapter 6
# Author: Kevin Pohl
# Last Change: 03.07.23
#-----------------------------------------------------

# Schreibe eine Funktion, die bei einem über die Konsole eingegebenen Text folgende Analysen durchführt:
# Den Text in einzelne Worte aufspaltet
# Eine Liste mit den Zeichenzahle eines jeden Wortes ausgibt
# Das Minimum bestimmt
# Das Maximum bestimmt
# Die Gesamtzeichenanzahl bestimmt
# Die Funktion soll vier Rückgabewerte haben: Zeichenzahlen-Liste, maximale Zeichenzahl, minimale Zeichenzahl und Gesamtzeichenzahl des Texts

#-----------------------------------------------------

def inputText():return str(input("Geben Sie den zu analysierenden Text ein: "))
def textAnalyse(text:str):
    listeWortlaengen=[]
    listeEinzeilworte=[]
    
    zulChr="abcdefghijklmnopqrstuvwxyzäöüß ";zulChr+= zulChr.upper() # Zusammenstellung von allen deutschen klein-,
    textV=""                                                         # Großbuchstaben und Leer als Trenner
    for zeichen in text:
        if zeichen in zulChr:
            textV+=zeichen
    listeEinzeilworte=textV.split()
    # listeEinzeilworte=textV.replace('.','')   # Nützliche Textfunktionen, wird hier nicht gebraucht
    # listeEinzeilworte=textV.count("a")        # dito
    # listeEinzeilworte=textV.find("ei")        # dito
    for eintrag in listeEinzeilworte:
        listeWortlaengen.append(len(eintrag))
    return listeWortlaengen,min(listeWortlaengen),max(listeWortlaengen),sum(listeWortlaengen)

beispielText="Dies ist ein Beispieltext, welcher zur Verringerung der Schreibarbeit abgelegt ist."

analyseErgebnis=textAnalyse(inputText())
print("Längen-Liste: ",analyseErgebnis[0],'\n',"Minlänge: ",analyseErgebnis[1],'\n',
      "Maxlänge: ",analyseErgebnis[2],'\n',"Gesamtlänge (ohne Satzzeichen): ",analyseErgebnis[3],sep='')
