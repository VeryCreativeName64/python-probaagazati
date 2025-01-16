def elso():
    print("Első feladat:")
    modszer=input("Kérek egy színkeverési módszert: ")
    kod=input("Kérem a kódot: ")

    if(modszer=="HEX"):
        if(len(kod)<6):
            print("Nem megfelelő hossz.")
        elif(len(kod)>6):
            print("Nem megfelelő hossz.")
        else:
            print("Megfelelő hossz.")
    
    elif(modszer=="RGB"):
        if(len(kod)<5):
            print("Nem megfelelő hossz.")
        elif(len(kod)>11):
            print("Nem megfelelő hossz.")
        else:
            print("Megfelelő hossz.")

    elif(modszer=="HSL"):
        if(len(kod)<7):
            print("Nem megfelelő hossz.")
        elif(len(kod)>13):
            print("Nem megfelelő hossz.")
        else:
            print("Megfelelő hossz.")

    else:
        print("Bonyolult kiszámolni.")