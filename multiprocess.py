from multiprocessing import Process
import time


def Spieler1(eingabe):
    spieler1boolean=False
    while spieler1boolean == False:
        if eingabe == 2:
            spieler1boolean=True
            print("richtige Zahl")
        else:
            print("falsche zahl")
            spieler1boolean=False
            

#def Spieler2(num):
   #pass

if __name__ == '__main__':
    eingabe = int(input("was ist 7-5?"))
    a = Process(target=Spieler1, args=int(eingabe),)
    #b = Process(target=Spieler1,)


    a.start()
    #b.start()

    print("processing...")

    a.join()
    #b.join()

    print("Done!")