import random

#initialisiert leeres SudokuFeld für Spieler1
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
data=[[]]

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

    if abfrage > 81:
        print("Eingabe ungültig")
        auslesenUNDerstellen()

    counterabfrage=0
    while counterabfrage < abfrage:
        x1 = random.randint(0,8)
        x2 = random.randint(0,8)
        if s1[x1][x2] != 0:
            s1[x1][x2]=0
            data[x1][x2]=0
            counterabfrage = counterabfrage +1
            
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
    
#gibt sudokubox im terminal aus
def printsudokubox1():
    print(s1[0][0],s1[0][1],s1[0][2],"|",s1[0][3],s1[0][4],s1[0][5],"|",s1[0][6],s1[0][7],s1[0][8])
    print(s1[1][0],s1[1][1],s1[1][2],"|",s1[1][3],s1[1][4],s1[1][5],"|",s1[1][6],s1[1][7],s1[1][8])
    print(s1[2][0],s1[2][1],s1[2][2],"|",s1[2][3],s1[2][4],s1[2][5],"|",s1[2][6],s1[2][7],s1[2][8])
    print("------+-------+------")
    print(s1[3][0],s1[3][1],s1[3][2],"|",s1[3][3],s1[3][4],s1[3][5],"|",s1[3][6],s1[3][7],s1[3][8])
    print(s1[4][0],s1[4][1],s1[4][2],"|",s1[4][3],s1[4][4],s1[4][5],"|",s1[4][6],s1[4][7],s1[4][8])
    print(s1[5][0],s1[5][1],s1[5][2],"|",s1[5][3],s1[5][4],s1[5][5],"|",s1[5][6],s1[5][7],s1[5][8])
    print("------+-------+------")
    print(s1[6][0],s1[6][1],s1[6][2],"|",s1[6][3],s1[6][4],s1[6][5],"|",s1[6][6],s1[6][7],s1[6][8])
    print(s1[7][0],s1[7][1],s1[7][2],"|",s1[7][3],s1[7][4],s1[7][5],"|",s1[7][6],s1[7][7],s1[7][8])
    print(s1[8][0],s1[8][1],s1[8][2],"|",s1[8][3],s1[8][4],s1[8][5],"|",s1[8][6],s1[8][7],s1[8][8])


Spieler1name = input("Name des 1. Spielers eingeben:")
Spieler2name = input("Name des 2. Spielers eingeben:")

auslesenUNDerstellen()
printsudokubox1()


#Funktion um Zahl ins ausgewähltes Feld einzutragen
def Spieler1():
    print(Spieler1name,"ist dran!")
    while True:
        try:
            auswahl = int(input("Was möchten Sie tun?\n1.Zahl eintragen\n2.Zahl löschen\n3.Passen\n4.Aufgeben"))
        except ValueError:
            print("Bitte nur Zahlen zwischen 1-4 eingeben")
            continue
        break
    if auswahl == 1:
        while True:
            try:
                zeile = int(input("welche zeile? 1-9")) -1
                spalte = int(input("welche spalte? 1-9")) -1
                eingabezahl = int(input("welche zahl 1-9"))
            except ValueError:
                print("Bitte nur Zahlen eingeben")
                continue
            break
        if s1[zeile][spalte] ==0:
            if kontrolleFeld(zeile,spalte,eingabezahl)==True:
                if eingabezahl > 0 and eingabezahl < 10:
                    s1[zeile][spalte]=eingabezahl
                    printsudokubox1()
                    if checkSudokuBox(s1):
                        sudokugewonnen(1)
                    else:
                        Spieler2()
                else:
                    print("Bitte Zahl zwischen 1 und 9 eingeben")
                    Spieler1()
            else:
                print("Falsche Eingabe")
                Spieler2()
        else:
            print("Vorgegebene Zahlen dürfen nicht verändert werden")
            print("Versuche ein leeres Feld")
            Spieler1()
    elif auswahl == 2:
        while True:
            try:
                zeile = int(input("welche zeile? 1-9")) -1
                spalte = int(input("welche spalte? 1-9")) -1
            except ValueError:
                print("Bitte nur Zahlen eingeben!")
                continue
            break

        if data[zeile][spalte]==0:
                s1[zeile][spalte]=0
        else:
            print("Vorgegebene Zahlen dürfen nicht gelöscht werden!")
            Spieler1()
    elif auswahl == 3:
        Spieler2()
    elif auswahl == 4:
        sudokugewonnen(2)
    else:
        print("Bitte Zahl zwischen 1 und 4 eingeben")
        Spieler1()

def Spieler2():
    print(Spieler2name,"ist dran!")
    while True:
        try:
            zeile = int(input("welche zeile? 1-9")) -1
            spalte = int(input("welche spalte? 1-9")) -1
            eingabezahl = int(input("welche zahl 1-9"))
        except ValueError:
            print("Bitte nur Zahlen eingeben")
            continue
        break
    if s1[zeile][spalte] !=0:
        if kontrolleFeld(zeile,spalte,eingabezahl)==True:
            if eingabezahl > 0 and eingabezahl < 10:
                s1[zeile][spalte]=eingabezahl
                printsudokubox1()
            else:
                print("Bitte Zahl zwischen 1 und 9 eingeben")
                Spieler2()
        else:
            print("Falsche Eingabe")
            Spieler1()
    else:
        print("Vorgegebene Zahlen dürfen nicht verändert werden")
        print("Versuche ein leeres Feld")
        Spieler2()


def sudokugewonnen(x):
    if x == 1:
        print(Spieler1name," hat gewonnen")
    else:
        print(Spieler2name," hat gewonnen!")

Spieler1()


#60% FERTIG
#to-dolist
#Bereits vorgegebene zahlen sollen sich abheben
#Timer sobald Sudoku geladen wurde bis es gelöst wird
#Wenn jemand das Sudoku gelöst hat soll es grafisch erkennbar sein
#INTERPROZESSKOMMUNIKATION
