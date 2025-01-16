from Auto import Auto
import fajlbeolvas

kocsi=fajlbeolvas.beolvas("auto.txt",[])

def flotta():
    print("III/Flotta:")
    db=0
    for i in range(0,(len(kocsi)),1):
        if((kocsi[i].nev)):
            db+=1
    print(f"Autók száma: {db}")
