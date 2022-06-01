def Spieler1():
    spieler1boolean=False
    while spieler1boolean == False:
        eingabe = int(input("was ist 7-5?"))
        if eingabe == 2:
                spieler1boolean=True
                print("richtige Zahl")
        else:
            print("falsche zahl")
            spieler1boolean=False

Spieler1()