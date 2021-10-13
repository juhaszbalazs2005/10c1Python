def feladat21():
    for i in range(1,6):
        for j in range(1,16):
            print(i*j, end=" ")
        print()

#feladat21()


def feladat22(a, b, c):
    for i in range(1,6):
        v=a*b*c
        print("a=", a, "b=", b, "c=", c, "V=", v)
        a = a+1
        b = b+2
        c = c+3

#feladat22(2,3,5)   

def feladat23(): #HF
    print()






#feladat23()
def feladat24(): #HF
    print()




#feladat24()

def feladat25(): #hf
    print()



#feladat25()



def feladat26():
    bekert=float(input("kérek egy számot! bekert="))
    osszeg= bekert
    while bekert<10:
        bekert=float(input("Kérek egy számot! bekert="))
        osszeg= osszeg+bekert
    print("A beolvasott számok összege:", osszeg)


feladat26()
