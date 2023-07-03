#-----------------------------------------------------
# Filename: Lineare_Regression.py
# Version: 1.0
# Function: Lineare Regression
# Author: Kevin Pohl
# Last Change: 29.06.23
#-----------------------------------------------------

def wurzel(zahl):import math;return math.sqrt(zahl)
def mittelwert(liste):return sum(liste)/len(liste)
def korrelation(liste1,liste2):cor=kovarianz(liste1,liste2)/(standardabweichung(liste1)*standardabweichung(liste2));return cor
def steigungGerade(liste1,liste2):steigung= standardabweichung(liste2) / standardabweichung(liste1) * korrelation(liste1,liste2);return steigung
def standardabweichung(liste):stabw=wurzel(varianz(liste));return stabw

# def kovarianz(liste1,liste2):
#     cov,i=0,0
#     while i < len(liste1):
#         cov+=(liste1[i]-mittelwert(liste1))*(liste2[i]-mittelwert(liste2))
#         i+=1
#     cov=cov/(len(liste1))
#     return cov

def kovarianz(liste1,liste2):
    cov,i=0,0
    for i in range(len(liste1)):
        cov+=(liste1[i]-mittelwert(liste1))*(liste2[i]-mittelwert(liste2))
    cov=cov/(len(liste1))
    return cov

def varianz(liste1):
    varianzQuadrat=0
    for element in liste1:
        varianzQuadrat+=(element-mittelwert(liste1))**2*(1/len(liste1))
    return varianzQuadrat

def schnittpunktY(liste1,liste2):
    schnittp=(-steigungGerade(liste1,liste2))*mittelwert(liste1)+mittelwert(liste2)
    return schnittp # -986

def linearGraph(Steigung,additiveKonstante,x): # f(x)=1x+1 -> f(x) = [Steigung] * x + [additive Konstante (y=0)]
    prognose=steigungGerade(Steigung,additiveKonstante) * x + schnittpunktY(Steigung,additiveKonstante)
    # print(steigungGerade(liste1,liste2),schnittpunktY(liste1,liste2),wunschtemp)
    return prognose

# ein Biergarten stellt fest, dass bei unterschiedlichen Außentemperaturen unterschiedlich viele Gäste kommen
# es werden 2 Listen angefertigt: die Temperatur en einem Tag und die Anzahl der Gäste an einem Tag,
# mithilfe von linearer Regression kann eine Prognose anhand der erwarteten Tagestemperatur vorgenommen werden:
Korrelationtabelle1=[28,23,32,35,29,30,27,34,32] # Tagestemperaturen
Korrelationtabelle2=[400,60,630,660,420,590,376,620,612] # Besucheranzahl
Abfragetabelle=[0,20,30,33,40,50,1000] # Temperatur Abfragetabelle
for i in range(len(Abfragetabelle)):
    print("Besucher bei "+str(Abfragetabelle[i])+" Grad:",int(linearGraph(Korrelationtabelle1,Korrelationtabelle2,Abfragetabelle[i])))
