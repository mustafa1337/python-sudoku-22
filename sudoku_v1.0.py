import random
import os
import datetime
from datetime import timedelta
import time

os.system("cls") #BEACHTEN!!!!!!!! WENN WINDOWS DANN os.system("cls") WENN LINUX DANN os.system("clear")

#initialisiert leeres 9x9 SudokuFeld für Spieler1
s1zeile1 = [0,0,0,0,0,0,0,0,0]
s1zeile2 = [0,0,0,0,0,0,0,0,0]
s1zeile3 = [0,0,0,0,0,0,0,0,0]
s1zeile4 = [0,0,0,0,0,0,0,0,0]
s1zeile5 = [0,0,0,0,0,0,0,0,0]
s1zeile6 = [0,0,0,0,0,0,0,0,0]
s1zeile7 = [0,0,0,0,0,0,0,0,0]
s1zeile8 = [0,0,0,0,0,0,0,0,0]
s1zeile9 = [0,0,0,0,0,0,0,0,0]
s1 = [s1zeile1,s1zeile2,s1zeile3,s1zeile4,s1zeile5,s1zeile6,s1zeile7,s1zeile8,s1zeile9]
dataX=[ #initialisiert dataX 2D-Liste damit später erstelltes Sudoku abgespeichert wird und dann gecheckt werden kann ob eine Zahl schon vorgegeben !=0 oder nicht vorgegeben wurde == 0, von auslesenUNDerstellen() Zeile 52 und 57
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
]

def auslesenUNDerstellen():
    sudokutxt = ['sudoku1.txt','sudoku2.txt'] #txt files mit fertigen sudokus
    fp = open(random.choice(sudokutxt)) #wählt zufällige textdatei aus zum auslesen
    lines = fp.readlines() 
    data = [[int(v) for v in line.split()] for line in lines] #speichert jede zahl in eine data Liste
    fp.close
    
    for i in range (9):
        for z in range (9):
            s1[i][z] = data[i][z] #erstellt eine sudokuliste zum spielen
    while True:
        try:
            abfrage = int(input("Wieviele Felder sollen entfernt werden? 1-81 ")) 
        except ValueError:
            print("\u001b[31;1m"+"Bitte nur Zahlen eingeben!"+"\033[0m")
            continue
        break

    if abfrage > 81 or abfrage < 1: #damit das programm nicht abstürzt
        print("\u001b[31;1m"+"Eingabe ungültig!"+"\033[0m")
        abfrage = 0
        auslesenUNDerstellen() #funktion startet von neu
    
    counterabfrage=0
    while counterabfrage < abfrage: #solange der counter unter abfrage ist wird wiederholt bzw. felder entfernt
        x1 = random.randint(0,8)
        x2 = random.randint(0,8)
        if s1[x1][x2] != 0:
            s1[x1][x2]=0
            counterabfrage = counterabfrage +1
    for i in range (9):
        for z in range (9):
            dataX[i][z] = s1[i][z] #die jetztige liste wo felder entfernt wurden werden nochmal in einer anderen liste gespeichert um später zu schauen welche felder anfangs vorgegeben waren 
                
def checkSudokuBox(grid):   #checkt ob das sudoku schon vollständig ausgefüllt ist -> sudoku ist fertig -> es gibt ein gewinner
    for row in range(0,9):
     for col in range(0,9):
        if grid[row][col]==0:
         return False
    return True
        
                  
       
def kontrolleFeld(x,y,zahl):
    tempvar = True
    
    #kontrolliert horizontal und vertikal alles durch(auch das eigene feld)
    for i in range(9):
        if zahl == s1[i][y] or zahl == s1[x][i]:
            tempvar = False

    #kontrolliert die restlichen 4 leeren Felder im Block des zu kontrollierenden Zahls
    if x == 0 or x == 3 or x == 6: #wenn sich zahl ganz oben im block befindet
        if y == 0 or y == 3 or y == 6: #wenn sich zahl oben im block und ganz links befindet
            if s1[x+1][y+1] == zahl or s1[x+1][y+2] == zahl or s1[x+2][y+1] == zahl or s1[x+2][y+2] == zahl:
                tempvar = False
        if y == 1 or y == 4 or y == 7: #oben und mitte
            if s1[x+1][y-1] == zahl or s1[x+2][y-1] == zahl or s1[x+1][y+1] == zahl or s1[x+2][y+1] == zahl:
                tempvar = False
        if y == 2 or y == 5 or y == 8: #oben und rechts
            if s1[x+1][y-1] == zahl or s1[x+1][y-2] == zahl or s1[x-2][y-1] == zahl or s1[x-2][y-2] == zahl:
                tempvar = False
    elif x == 1 or x == 4 or x == 7: #wenn sich zahl in der mitte vom block befindet
        if y == 0 or y == 3 or y == 6: #mitte und links
            if s1[x-1][y+1] == zahl or s1[x-1][y+2] == zahl or s1[x+1][y+1] == zahl or s1[x+1][y+2] == zahl:
                tempvar = False
        if y == 1 or y == 4 or y == 7: #mitte und mitte
            if s1[x-1][y-1] == zahl or s1[x-1][y+1] == zahl or s1[x+1][y-1] == zahl or s1[x+1][y+1] == zahl:
                tempvar = False
        if y == 2 or y == 5 or y == 8: #mitte und rechts
            if s1[x-1][y-1] == zahl or s1[x-1][y-2] == zahl or s1[x+1][y-1] == zahl or s1[x+1][y-2] == zahl:
                tempvar = False
    elif x == 2 or x == 5 or x == 8: #wenn sich zahl unten vom block befindet
        if y == 0 or y == 3 or y == 6: #unten und links
            if s1[x-1][y+1] == zahl or s1[x-1][y+2] == zahl or s1[x-2][y+1] == zahl or s1[x-2][y-2] == zahl:
                tempvar = False
        if y == 1 or y == 4 or y == 7: #unten und mitte
            if s1[x-1][y-1] == zahl or s1[x-2][y-1] == zahl or s1[x-1][y+1] == zahl or s1[x-2][y+1] == zahl:
                tempvar = False
        if y == 2 or y == 5 or y == 8: #unten und rechts
            if s1[x-1][y-1] == zahl or s1[x-1][y-2] == zahl or s1[x-2][y-1] == zahl or s1[x-2][y-2] == zahl:
                tempvar = False
    if tempvar == True:
        return True
    else:
        return False

def printsudokubox2():
    for i in range(9):
        for z in range(9):
            if z == 0: #printet am anfang jeder zeile die Angabe der Zeilennummer
                print(i+1,end=". ")
            if dataX[i][z] == 0: #wenn die Zahl nicht vorgegeben ist(bei datax mit 0 abgespeichert) dann ohne Farben printen
                if (z+1) % 3 == 0: #die index von z (spalte) erhöht um 1 um 3. spalten zu filtern mit %3 da ansonten mit 0 1 2 nicht funktionieren würde
                    if z == 8 and (i+1) % 3 == 0 and i !=8: #wenn letzte spalte in der Zeile UND jede 3. zeile UND NICHT allerletzte Zeile dann große Trennwand
                        print(s1[i][z],end="\n")
                        print("   ------+-------+------")
                    elif z == 8: #wenn letzte spalte fängt neue Zeile an (letzte Spalte ist immer index 8)
                        print(s1[i][z],end="\n")
                    else: #jede 3. Spalte kommt eine kleine Trennwand mit | 
                        print(s1[i][z],"| ",end="")
                else: #wenn keine Trennwand erforderlich dann Zahl normal mit Abstand zur nächsten printen in der selben Zeile (end="")
                    print(s1[i][z],"",end="")
            else: #wenn Zahl vorgegeben ist (bei datax nicht mit 0 abgespeichert) dann mit Farbe printen (HERVORHEBEN)
                if (z+1) % 3 == 0: 
                    if z == 8 and (i+1) % 3 == 0 and i !=8: 
                        print("\u001b[32m"+str(s1[i][z])+"\033[0m",end="\n")
                        print("   ------+-------+------")
                    elif z == 8: 
                        print("\u001b[32m"+str(s1[i][z])+"\033[0m",end="\n")
                    else: 
                        print("\u001b[32m"+str(s1[i][z])+"\033[0m","| ",end="")
                else: 
                    print("\u001b[32m"+str(s1[i][z])+"\033[0m","",end="")
                

#Funktion um Zahl ins ausgewähltes Feld einzutragen
def Spieler1():
    print("\u001b[34;1m"+Spieler1name+"\033[0m","ist dran!")
    printsudokubox2() #printet erstmal sudokubox aus 
    while True: 
        try:
            auswahl = int(input("Was möchten Sie tun?\n1.Zahl eintragen\n2.Zahl löschen\n3.Passen\n4.Aufgeben ")) #abfrage welche Option
        except ValueError:
            print("\u001b[31;1m"+"Bitte nur Zahlen zwischen 1-4 eingeben"+"\033[0m") #catcht error meldung
            continue
        break
    if auswahl == 1: #wenn 1 eingegeben wurde wird das ausgeführt
        while True:
            try:
                zeile = int(input("Welche Zeile? 1-9 ")) -1 #-1 weil der Spieler nichts vom Index 0-8 der Liste weiß. Er kennt nur Zeile 1-9 und gibt deshalb auch 1-9 ein
                spalte = int(input("Welche Spalte? 1-9 ")) -1
                eingabezahl = int(input("Welche Zahl 1-9 "))
            except ValueError:
                print("\u001b[31;1m"+"Bitte nur Zahlen eingeben"+"\033[0m") #catcht error
                continue
            break
        if zeile < 0 or zeile > 8 or spalte < 0 or spalte > 8: #catcht error
            print("\u001b[31;1m"+"Bitte Zahl zwischen 1 und 9 eingeben"+"\033[0m")
            Spieler1()

        if s1[zeile][spalte] == 0: #wenn das Feld keine Zahl ist also noch nicht ausgefüllt wurde
            if kontrolleFeld(zeile,spalte,eingabezahl)==True: #kontrolliert ob die eingegebene zahl im feld konsistent bzw richtig ist
                if eingabezahl > 0 and eingabezahl < 10: #catcht fehlermerldung
                    s1[zeile][spalte]=eingabezahl 
                    printsudokubox2()
                    if checkSudokuBox(s1): #checkt ob sudokubox komplett fertig ist
                        sudokugewonnen(1)
                    else:
                        Spieler2() #spieler 2 ist dran
                else:
                    print("\u001b[31;1m"+"Bitte Zahl zwischen 1 und 9 eingeben"+"\033[0m")
                    Spieler1()
            else:
                print("\u001b[31;1m"+"Falsche Zahl"+"\033[0m")
                Spieler2()
        else:
            print("\u001b[31;1m"+"Vorgegebene Zahlen dürfen nicht verändert werden!"+"\033[0m")
            print("\u001b[31;1m"+"Versuche ein leeres Feld"+"\033[0m")
            Spieler1()
    elif auswahl == 2:
        while True:
            try:
                zeile = int(input("Welche zeile? 1-9 ")) -1
                spalte = int(input("Welche spalte? 1-9 ")) -1
            except ValueError:
                print("\u001b[31;1m"+"Bitte nur Zahlen eingeben!"+"\033[0m")
                continue
            break

        if zeile < 0 or zeile > 8 or spalte < 0 or spalte > 8:
            print("\u001b[31;1m"+"Bitte Zahl zwischen 1 und 9 eingeben."+"\033[0m")
            Spieler1()
            
        if dataX[zeile][spalte]==0: #guckt ob das Feld Anfangs vorgegeben war oder nicht weil es 0 wäre dann
                s1[zeile][spalte]=0 #setzt das jeweilige Feld dann auf 0
                Spieler1()
        else:
            print("\u001b[31;1m"+"Vorgegebene Zahlen dürfen nicht gelöscht werden!"+"\033[0m") #wenn es nicht 0 ist dann war das feld vorgegeben
            Spieler1()
    elif auswahl == 3: #übergibt den Zug an Spieler 2
        print("Du übergibst dein Zug an",Spieler2name)
        Spieler2()
    elif auswahl == 4:
        sudokugewonnen(2) #wenn man aufgibt gewinnt Spieler 2
    else:
        print("\u001b[31;1m"+"Bitte Zahl zwischen 1 und 4 eingeben"+"\033[0m") #Wenn man Anfangs sich nicht für Option 1-4 entscheidet und eine andere Zahl eingibt wird Funktion von neu wiederholt
        Spieler1()

def Spieler2(): #genau das gleiche wie bei Spieler1() nur anders herum mit der Spieler1() und Spieler2() funktion
    print("\u001b[34;1m"+Spieler2name+"\033[0m","ist dran!")
    printsudokubox2()
    while True:
        try:
            auswahl = int(input("Was möchten Sie tun?\n1.Zahl eintragen\n2.Zahl löschen\n3.Passen\n4.Aufgeben "))
        except ValueError:
            print("\u001b[31;1m"+"Bitte nur Zahlen zwischen 1-4 eingeben"+"\033[0m")
            continue
        break
    if auswahl == 1:
        while True:
            try:
                zeile = int(input("Welche Zeile? 1-9 ")) -1
                spalte = int(input("Welche Spalte? 1-9 ")) -1
                eingabezahl = int(input("Welche Zahl 1-9 "))
            except ValueError:
                print("\u001b[31;1m"+"Bitte nur Zahlen von 1-9 eingeben"+"\033[0m")
                continue
            break
        if zeile < 0 or zeile > 8 or spalte < 0 or spalte > 8:
            print("\u001b[31;1m"+"Bitte Zahl zwischen 1 und 9 eingeben"+"\033[0m")
            Spieler2()

        if s1[zeile][spalte] ==0:
            if kontrolleFeld(zeile,spalte,eingabezahl)==True:
                if eingabezahl > 0 and eingabezahl < 10:
                    s1[zeile][spalte]=eingabezahl
                    printsudokubox2()
                    if checkSudokuBox(s1):
                        sudokugewonnen(1)
                    else:
                        Spieler1()
                else:
                    print("\u001b[31;1m"+"Bitte Zahl zwischen 1 und 9 eingeben."+"\033[0m")
                    Spieler2()
            else:
                print("\u001b[31;1m"+"Falsche Zahl"+"\033[0m")
                Spieler1()
        else:
            print("\u001b[31;1m"+"Vorgegebene Zahlen dürfen nicht verändert werden!"+"\033[0m")
            print("\u001b[31;1m"+"Versuche ein leeres Feld"+"\033[0m")
            Spieler2()
    elif auswahl == 2:
        while True:
            try:
                zeile = int(input("Welche Zeile? 1-9 ")) -1
                spalte = int(input("Welche Spalte? 1-9 ")) -1
            except ValueError:
                print("\u001b[31;1m"+"Bitte nur Zahlen eingeben!"+"\033[0m")
                continue
            break
        if zeile < 0 or zeile > 8 or spalte < 0 or spalte > 8:
            print("\u001b[31;1m"+"Bitte Zahl zwischen 1 und 9 eingeben"+"\033[0m")
            Spieler2()

        if dataX[zeile][spalte]==0:
                s1[zeile][spalte]=0
                Spieler2()
        else:
            print("\u001b[31;1m"+"Vorgegebene Zahlen dürfen nicht gelöscht werden!"+"\033[0m")
            Spieler2()
    elif auswahl == 3: 
        print("Du übergibst dein Zug an",Spieler1name)
        Spieler1()
    elif auswahl == 4:
        sudokugewonnen(1)
    else:
        print("\u001b[31;1m"+"Bitte Zahl zwischen 1 und 4 eingeben"+"\033[0m")
        Spieler2()


def sudokugewonnen(x):
    if x == 1: #wenn Spieler 1 gewonnen hat wird das ausgeführt
        zeitmessung_ende_spieler1 = datetime.datetime.now()
        print("\033[1;96m"+"###############################################") #Zeit wird nochmal gespeichert und die differenz wird gebildet und in Sekunden ausgegeben sowie Farbig
        print("\033[1;96m"+Spieler1name,"HAT GEWONNEN und dafür",round(timedelta.total_seconds(zeitmessung_ende_spieler1-zeitmessung_anfang_spieler1)),"Sekunden gebraucht!")
        print("\033[1;96m"+"###############################################")

    else: #wenn spieler2 gewonnen hat
        zeitmessung_ende_spieler2 = datetime.datetime.now()
        print("\033[1;96m"+"###############################################") 
        print("\033[1;96m"+Spieler2name,"HAT GEWONNEN und dafür",round(timedelta.total_seconds(zeitmessung_ende_spieler2-zeitmessung_anfang_spieler2)),"Sekunden gebraucht!")
        print("\033[1;96m"+"###############################################")

#AUSFÜHRUNG DES CODES
Spieler1name = input("Name des 1. Spielers eingeben: ")
Spieler2name = input("Name des 2. Spielers eingeben: ")
auslesenUNDerstellen()
zeitmessung_anfang_spieler1 = datetime.datetime.now() #Zeit zum Zeitpunkt des Spielstarts wird gespeichert
zeitmessung_anfang_spieler2 = zeitmessung_anfang_spieler1  #ebenso für Spieler 2
Spieler1()
