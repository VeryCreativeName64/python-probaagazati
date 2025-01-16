class Auto:
    def __init__(self,nev:str="",datum:int=0):
        self.nev=nev
        self.datum=int(datum)

    def __str__(self):
        return(f"Auto adatok:\n"
               f"Név:{self.nev}\n"
               f"Dátum:{self.datum}\n"
               f"*********************\n"
               f"\n")
        