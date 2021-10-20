from random import *

def feladat45():
    a=randint(18,69)
    print("A =", a)
    b=randint(18,69)
    print("B =", b)
    nagyobb = max(a,b)
    kissebb = min(a,b)
    print("Hányaduk: ",nagyobb/kissebb)
    print("Hányados: ",nagyobb//kissebb)

def feladat47():
    szorzat=1
    cv=1
    while cv<=10:
        gen=randint(0,100)
        if gen%2==0:
            szorzat*=gen
            print(gen,"\t",szorzat)
            cv=cv+1
        
def feladat48():
    gen=randint(10,50)
    print(gen, end=" ")
    while gen != 25:
        gen= randint(10,50)
        print(gen, end=" ")
    print()

#HÁZI FELADATOK


def feladat41():
    gen=randint(0,9999)
    szamok=1
    print(gen, end=", ")
    while szamok<=10:
        gen=randint(0,9999)
        szamok=szamok+1
        print(gen, end=", ")

def feladat42():
    gen=randint(0,20)
    szamok=1
    print(gen, end=", ")
    while szamok<=20:
        gen=randint(0,20)
        szamok=szamok+1
        print(gen, end=", ")

def feladat43():
    gen=randint(25,50)
    szamok=1
    print(gen, end=", ")
    while szamok<=15:
        gen=randint(25,50)
        szamok=szamok+1
        print(gen, end=", ")

def feladat44():
    a=randint(10,50)
    b=randint(10,50)
    print("A számok szorzata: ",a*b)


