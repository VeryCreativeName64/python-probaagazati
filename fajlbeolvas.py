from Auto import Auto
def beolvas(fajlnev,kocsi_lista=[]):
    fajlom=open(fajlnev,"r",encoding="UTF-8")
    elso_sor=fajlom.readline()
    tobbi_sor=fajlom.readlines()

    for i in range(0,len(tobbi_sor),1):
        sor=tobbi_sor[i].strip()
        sor_lista=sor.split(":")
        kocsim=Auto(sor_lista[0],int(sor_lista[1]))
        kocsi_lista.append(kocsim)
    fajlom.close()
