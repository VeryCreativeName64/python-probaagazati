import random

def hettelOszthato():
    lista=[]
    for i in range(1,51):
        szam=random.randint(1,100)
        lista.append(szam)
    print("A lista elemei:")
    print(*lista, sep=", ")
    db=0
    for i in range(len(lista)):
        if(lista[i]%7==0):
            db+=1
    return db
    