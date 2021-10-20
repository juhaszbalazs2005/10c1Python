
def feladat1():
    print("FELADAT 1: írj egy programot, ami beolvas egy valós számot, majd kiírja háromszorosát!")
    a = int(input("Adj meg egy valós számot! a="))
    print("A szám 3x-a =", a*3)
    print()

def feladat2():
    print("FELADAT 2: Írj egy programot, amely beolvassa egy háromszög egyik oldalát és ahoz tartozó magasságot, majd kiírja a háromszög területét!")
    a = int(input("Adj meg egy számot! a="))
    m = int(input("Adj meg egy másik számot! m="))
    osszeg= a*m
    print("A háromszög területe:",osszeg/2)
    print()

def feladat3():
    print("FELADAT 3: Írj egy programot, ami eldönti egy bekért számról hogy osztható-e öttel?")
    a = int(input("Adj meg egy valós számot! a="))
    if a%5==0:
        print("A szám osztható 5-el")
    else:
        print("A szám nem osztható 5-el")
    print()

def feladat4():
    print("FELADAT 4: Írj egy programot, amely egy beolvasott számról eldönti, hogy -50 és 20 között van-e!")
    a = int(input("Adj meg egy valós számot! a="))
    if a <-50 or a>20:
        print("A szám nincs -50 és 20 között")
    else:
        print("A szám -50 és 20 között van")
    print()

def feladat5():
    print("FELADAT 5: Írasd ki az első húsz négyzetszámot egymás mellé!")
    for i in range(1,21):
        print(i*i, end=" ")
    print()



def feladat6():
    print("FELADAT 6: Írasd ki azokat a számokat 1-től 30-ig egymás mellé, amelyek hárommal osztva 2 maradékot adnak")
    for i in range(1,21):
        if i%3==2:
            print(i, end=" ")
        else:
            print(end="")
    print()


def feladat7():
    print("FELADAT 7: Írasd ki a 9-es szorzótábla első 25 eleméből azokat, amik 4-gyel oszthatóak!")
    for i in range(1,26):
        if 9*i%4==0:
            print(9*i, end=" ")
    print()

feladat1()
feladat2()
feladat3()
feladat4()
feladat5()
feladat6()
feladat7()
