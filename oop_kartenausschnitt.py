#-----------------------------------------------------
# Filename: oop_kartenausschnitt.py
# Version: 1.0
# Author: Kevin Pohl
# Last Change: 03.08.23
#-----------------------------------------------------

from mpl_toolkits.basemap import Basemap
from matplotlib.pyplot import figure,plot,text,show
from numpy import arange

# Eselsbrücke: Durch Greenwich, (Lon)don läuft die (Lon)gitude 0, der (A)equator ist eine L(a)titude.
# ---------------------------------------------------------------------------------------------------
# Variablen in Klassen = Attribute
# Funktionen in Klassen = Methoden

class MapApp():
    # es ist mein persönlicher Geschmack, hier Werte anzulegen, die ich unverändert in anderen Klassen abrufen möchte
    # und kleine Einstellungsvariablen, wie z.B. debug=True, die für alle Instanzen unverändert gelten sollen
    cmfrominch=1/2.54 # umrechenfaktor cm je inch
    window_size=20 # Kantenlänge des zu erstellenden Fensters in cm
    
    # wird wie unten app = MapApp() aufgerufen wird die Methode mit dem Namen __init__ immer automatisch zuerst gestartet
    def __init__(self): 
        self.window=None    # Variable window wird initialisiert
        self.map=None       # Variable map wird initialisiert
        
        # Kartenausschnitt unten links (3,55) bis oben rechts (46,72)
        self.lowerleftlon=3.0
        self.lowerleftlat=55.0     
        self.upperrightlon=46.0     
        self.upperrightlat=72.0
        
        self.projection='lcc' # Lambert Conformal Conic map
        
        # Aufösung ist (c)rude), (l)ow, (i)ntermediate, (h)igh), (f)ull oder None. Bei None erzeugen alle
        # Methoden die von den Kartendaten abhängen (drawcoastlines,drawcountries,...) einen Fehler
        # Die Auflösung verringert sich um ca. 80% je geringerer Qualität
        self.resolution='i'
        self.plotter() # springt in die Funktion plotter
        self.mapper() # springt in die Funktion mapper
        self.abisko=MapPoint(name="Abisko",lon=18.8312,lat=68.3495) # weist dem Attribut abisko die Klasse MapPoint zu
        self.pointplotter(self.abisko) # zeichnet abisko in die Karte ein
        show()
        pass

    def pointplotter(self,point:"MapPoint"):
        x, y = self.map(point.lon,point.lat)
        plot(x, y, point.marker, markersize=point.marker_size)
        text(x, y, ' '+point.name, fontsize=point.fontsize)
        pass
    
    def plotter(self):
        # bereits in __init__ initialisiertes self.window wird hier erstmalig in ein matplotlib.figure.Figure
        # Objekt umgewandelt, dieses enthält die gewünschte Fenstergröße in pixel, die Größe wird nativ in inch
        # angegeben, wird hier aber von cm in inch umgerechnet
        self.window=figure(figsize=(self.window_size * self.cmfrominch,
                                    self.window_size * self.cmfrominch))
        pass
        
    def mapper(self):
        # bereits in __init__ initialisiertes self.map wird hier erstmalig als Basemap-Objekt definiert und
        # mit den vorher festgelegten Eigenschaften erzeugt
        self.map = Basemap(projection=self.projection,  # llc
                    resolution=self.resolution,         # i
                    llcrnrlon=self.lowerleftlon,        # 3.0
                    llcrnrlat=self.lowerleftlat,        # 55.0
                    urcrnrlon=self.upperrightlon,       # 46.0
                    urcrnrlat=self.upperrightlat,       # 72.0

                    # lat_0 ist eine perspektivische Verzerrung der Karte aus Sicht einer Latitude der Welt
                    # z.B. des Äquators, Bereich: 89.99 bis 0.01; -0.01 bis -89.99 Aussehen der Kartenverzerrung:
                    # bei +89 Fächern die Latituden von Norden nach Süden auf,
                    # bei +0.01 sehen sie sehr gerade aus,
                    # bei -89 fächern sie von unten nach oben auf.
                    # Das ist KEINE falsche Darstellung der Latituden, sondern die zugrundeliegende Karte wurde
                    # entsprechend verzerrt.
                    # Sehr einfach formuliert: man kann die Latitude einstellen die auf dem Bild perfekt vertikal
                    # sein soll, diese muss aber nicht Teil des Bildes sein.
                    # Die Formel wählt hierfür die rechnerische Mitte der eingegrenzten Koordinaten.
                    lat_0=(self.lowerleftlat+self.upperrightlat)*0.5,
                    # Hier ebenfalls einfach: Die hier eingestellte Longitude ist auf dem Bild perfekt horizontal,
                    # auch diese diese muss nicht Teil des Bildes sein.
                    # Auch hierfür wählt die Formel die rechnerische Mitte der eingegrenzten Koordinaten.
                    lon_0=(self.lowerleftlon+self.upperrightlon)*0.5)

        # es werden alle 5° Latituden vom Nordpol(90) bis zum Südpol(-90) eingetragen, Null ist der Äquator
        # labels = Latitudenbeschriftung anzeigen - links, rechts, über, unter der Karte - Mehrfachauswahl ist möglich
        self.map.drawparallels(arange(-90.,90.,5.),labels=[1,0,0,0])
        
        # Longitude: normalerweise von -180° bis +180°, hier von 0° bis 360° um die Welt rechtsherum (von Köln nach Berlin)
        # Zeitversatz lässt sich hiermit genauer als mit Zeitzonen berechnen (z.B. der exakte Zeitversatz
        # des Sonnenaufgangs zwischen zwei Orten, hierbei entsprechen 15° einer Stunde Zeitunterschied). Diese Berechnung
        # wird aufgrund der Erdkrümmung ungenau, wenn die Latituden zu stark abweichen (z.B. Europa zu Äquator).
        # Nullmeridian ist der Mittelpunkt des Teleskops im Royal Greenwich Observatory in Greenwich, London
        self.map.drawmeridians(arange(0.,360.,5.),labels=[0,0,0,1]) # zeichne alle vorkommenden Meridiane in 5° Schritten
        self.map.etopo(alpha=0.6) # topographische Karte mit 60% alpha
        
        # Exkurs Farben=Rot,Grün,Blau = #RR|GG|BB = #00|00|00 = 00 bis ff je platz in hex ergeben 0 bis 255 je Farbe
        # "#0000ff" ist null Rot, null Grün, 255 Blau; "#ffff00" ist gelb, "#00ffff" ist cyan, diese Regeln gelten
        # für beleuchtete Farben (Monitor) das Prinzip heißt additive Farbmischung, man beginnt mit
        # schwarz = "kein Licht" = "#000000" und endet bei weiß = "alle Farbspektren" = "#ffffff" 
        self.map.drawcountries(color='#ff0000')
        self.map.drawrivers(color='#0000ff')
        pass

class MapPoint():
    # eine eigene Klasse zur Definition eines einzuzeichnenden Punktes auf der Karte, der Aufruf ist:
    # MapPoint(Name als String,Longitude als Float oder Int, Latitude als Float oder Int)
    # alle relevanten Eigenschaften sind in der __init__ definiert, eine Variable oder ein Attribut
    # können anschließend dieser Klasse zugeordnet werden
    def __init__(self,name:str,lon:float|int,lat:float|int)-> "MapPoint":
        self.name=str(name) # es soll sichergestellt werden, dass der übergebene Name wirklich als String gespeichert wird
        self.lon=float(lon) # dito als float
        self.lat=float(lat) # dito als Float
        self.marker='ok'    # das ok-Zeichen wird später als Punkt auf der Karte dargestellt
        self.marker_size=3  # die Größe des Punktes
        self.fontsize=6     # die Größe des Namens, hier:"Abisko"
        self.TypeVar="MapPoint"
        pass
    pass


# alles nach dem folgenden if wird nur ausgeführt, wenn diese Datei geöffnet wurde, wird das Modul in eine
# andere Datei importiert (so wie z.B. bei "import numpy as np") ist der nachfolgende Code gegenstandslos
# so kann man seinen eigenen Code testen, kommt aber den Nutzern meines Codes nicht in die Quere
if __name__=='__main__':

    app=MapApp()
    

