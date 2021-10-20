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

"""
41. Generálj 10 véletlenszámot és írasd ki a képernyőre vesszővel elválasztva!

42. Generálj 20 véletlenszámot 0 és 20 között, és írasd ki a képernyőre vesszővel elválasztva!

43. Generálj 15 véletlenszámot 25 és 50 között, és írasd ki a képernyőre vesszővel 
elválasztva! 

44. Generálj két egész véletlen számot 10 és 50 között, írasd ki a szorzatát! 
"""