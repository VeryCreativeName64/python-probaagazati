import random

def hettelOszthato():
    lista=[]
    for _ in range(1,51):
        szam=random.randint(1,100)
        lista.append(szam)
    print("A lista elemei:")
    print(*lista, sep=", ")
    db=0
    for szam in lista:
        if(szam%7==0):
            db+=1
    return db
    