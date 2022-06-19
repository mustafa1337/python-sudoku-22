import random
import os

os.system("cls") #BEACHTEN!!!!!!!! WENN WINDOWS DANN "cls" WENN LINUX DANN "clear"

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
    fp = open('sudoku1.txt')
    lines = fp.readlines()
    data = [[int(v) for v in line.split()] for line in lines]
    
    for i in range (9):
        for z in range (9):
            s1[i][z] = data[i][z]
    while True:
        try:
            abfrage = int(input("Wieviele Felder sollen entfernt werden?"))
        except ValueError:
            print("Bitte nur Zahlen eingeben")
            continue
        break

    if abfrage > 81 or abfrage < 0:
        print("Eingabe ungültig")
        auslesenUNDerstellen()

    counterabfrage=0
    while counterabfrage < abfrage:
        x1 = random.randint(0,8)
        x2 = random.randint(0,8)
        if s1[x1][x2] != 0:
            s1[x1][x2]=0
            counterabfrage = counterabfrage +1

    for i in range (9):
        for z in range (9):
            dataX[i][z] = s1[i][z]
            
#def generateSudoku():
 #   for i in range(0,9):
  #      for z in range(0,9):
   #         if s1[i][z]==0:
    #            zrand = random.randint(1,9)
     #           if kontrolleFeld(i,z,zrand):
      #              s1[i][z]=zrand
       #             generateSudoku()
                
def checkSudokuBox(grid):  
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

    #kontrolliert die blöcke (3x3)
    if x == 0 or x == 3 or x == 6:
        if y == 0 or y == 3 or y == 6:
            if s1[x+1][y+1] == zahl or s1[x+1][y+2] == zahl or s1[x+2][y+1] == zahl or s1[x+2][y+2] == zahl:
                tempvar = False
        if y == 1 or y == 4 or y == 7:
            if s1[x+1][y-1] == zahl or s1[x+2][y-1] == zahl or s1[x+1][y+1] == zahl or s1[x+2][y+1] == zahl:
                tempvar = False
        if y == 2 or y == 5 or y == 8:
            if s1[x+1][y-1] == zahl or s1[x+1][y-2] == zahl or s1[x-2][y-1] == zahl or s1[x-2][y-2] == zahl:
                tempvar = False
    elif x == 1 or x == 4 or x == 7:
        if y == 0 or y == 3 or y == 6:
            if s1[x-1][y+1] == zahl or s1[x-1][y+2] == zahl or s1[x+1][y+1] == zahl or s1[x+1][y+2] == zahl:
                tempvar = False
        if y == 1 or y == 4 or y == 7:
            if s1[x-1][y-1] == zahl or s1[x-1][y+1] == zahl or s1[x+1][y-1] == zahl or s1[x+1][y+1] == zahl:
                tempvar = False
        if y == 2 or y == 5 or y == 8:
            if s1[x-1][y-1] == zahl or s1[x-1][y-2] == zahl or s1[x+1][y-1] == zahl or s1[x+1][y-2] == zahl:
                tempvar = False
    elif x == 2 or x == 5 or x == 8:
        if y == 0 or y == 3 or y == 6:
            if s1[x-1][y+1] == zahl or s1[x-1][y+2] == zahl or s1[x-2][y+1] == zahl or s1[x-2][y-2] == zahl:
                tempvar = False
        if y == 1 or y == 4 or y == 7:
            if s1[x-1][y-1] == zahl or s1[x-2][y-1] == zahl or s1[x-1][y+1] == zahl or s1[x-2][y+1] == zahl:
                tempvar = False
        if y == 2 or y == 5 or y == 8:
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
                

Spieler1name = input("Name des 1. Spielers eingeben:")
Spieler2name = input("Name des 2. Spielers eingeben:")

auslesenUNDerstellen()


#Funktion um Zahl ins ausgewähltes Feld einzutragen
def Spieler1():
    print("\u001b[34;1m"+Spieler1name+"\033[0m","ist dran!")
    printsudokubox2()
    while True:
        try:
            auswahl = int(input("Was möchten Sie tun?\n1.Zahl eintragen\n2.Zahl löschen\n3.Passen\n4.Aufgeben"))
        except ValueError:
            print("\u001b[31;1m"+"Bitte nur Zahlen zwischen 1-4 eingeben"+"\033[0m")
            continue
        break
    if auswahl == 1:
        while True:
            try:
                zeile = int(input("welche zeile? 1-9")) -1
                spalte = int(input("welche spalte? 1-9")) -1
                eingabezahl = int(input("welche zahl 1-9"))
            except ValueError:
                print("\u001b[31;1m"+"Bitte nur Zahlen eingeben"+"\033[0m")
                continue
            break
        if s1[zeile][spalte] ==0:
            if kontrolleFeld(zeile,spalte,eingabezahl)==True:
                if eingabezahl > 0 and eingabezahl < 10:
                    s1[zeile][spalte]=eingabezahl
                    printsudokubox2()
                    if checkSudokuBox(s1):
                        sudokugewonnen(1)
                    else:
                        Spieler2()
                else:
                    print("\u001b[31;1m"+"Bitte Zahl zwischen 1 und 9 eingeben"+"\033[0m")
                    Spieler1()
            else:
                print("\u001b[31;1m"+"Falsche Zahl"+"\033[0m")
                Spieler2()
        else:
            print("\u001b[31;1m"+"Vorgegebene Zahlen dürfen nicht verändert werden"+"\033[0m")
            print("\u001b[31;1m"+"Versuche ein leeres Feld"+"\033[0m")
            Spieler1()
    elif auswahl == 2:
        while True:
            try:
                zeile = int(input("welche zeile? 1-9")) -1
                spalte = int(input("welche spalte? 1-9")) -1
            except ValueError:
                print("\u001b[31;1m"+"Bitte nur Zahlen eingeben!"+"\033[0m")
                continue
            break

        if dataX[zeile][spalte]==0:
                s1[zeile][spalte]=0
                Spieler1()
        else:
            print("\u001b[31;1m"+"Vorgegebene Zahlen dürfen nicht gelöscht werden!"+"\033[0m")
            Spieler1()
    elif auswahl == 3:
        print("Du übergibst dein Zug an ",Spieler2name)
        Spieler2()
    elif auswahl == 4:
        sudokugewonnen(2)
    else:
        print("\u001b[31;1m"+"Bitte Zahl zwischen 1 und 4 eingeben"+"\033[0m")
        Spieler1()

def Spieler2():
    print("\u001b[34;1m"+Spieler2name+"\033[0m","ist dran!")
    printsudokubox2()
    while True:
        try:
            auswahl = int(input("Was möchten Sie tun?\n1.Zahl eintragen\n2.Zahl löschen\n3.Passen\n4.Aufgeben"))
        except ValueError:
            print("\u001b[31;1m"+"Bitte nur Zahlen zwischen 1-4 eingeben"+"\033[0m")
            continue
        break
    if auswahl == 1:
        while True:
            try:
                zeile = int(input("welche zeile? 1-9")) -1
                spalte = int(input("welche spalte? 1-9")) -1
                eingabezahl = int(input("welche zahl 1-9"))
            except ValueError:
                print("\u001b[31;1m"+"Bitte nur Zahlen eingeben"+"\033[0m")
                continue
            break
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
                    print("\u001b[31;1m"+"Bitte Zahl zwischen 1 und 9 eingeben"+"\033[0m")
                    Spieler2()
            else:
                print("\u001b[31;1m"+"Falsche Zahl"+"\033[0m")
                Spieler1()
        else:
            print("\u001b[31;1m"+"Vorgegebene Zahlen dürfen nicht verändert werden"+"\033[0m")
            print("\u001b[31;1m"+"Versuche ein leeres Feld"+"\033[0m")
            Spieler2()
    elif auswahl == 2:
        while True:
            try:
                zeile = int(input("welche zeile? 1-9")) -1
                spalte = int(input("welche spalte? 1-9")) -1
            except ValueError:
                print("\u001b[31;1m"+"Bitte nur Zahlen eingeben!"+"\033[0m")
                continue
            break

        if dataX[zeile][spalte]==0:
                s1[zeile][spalte]=0
                Spieler2()
        else:
            print("\u001b[31;1m"+"Vorgegebene Zahlen dürfen nicht gelöscht werden!"+"\033[0m")
            Spieler2()
    elif auswahl == 3:
        print("Du übergibst dein Zug an ",Spieler2name)
        Spieler1()
    elif auswahl == 4:
        sudokugewonnen(1)
    else:
        print("\u001b[31;1m"+"Bitte Zahl zwischen 1 und 4 eingeben"+"\033[0m")
        Spieler2()


def sudokugewonnen(x):
    if x == 1:
        print(Spieler1name," hat gewonnen")
    else:
        print(Spieler2name," hat gewonnen!")

Spieler1()


#70% FERTIG
#to-dolist
#Timer sobald Sudoku geladen wurde bis es gelöst wird
#Wenn jemand das Sudoku gelöst hat soll es grafisch erkennbar sein
#INTERPROZESSKOMMUNIKATION

