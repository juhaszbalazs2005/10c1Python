from random import *
lista1 = []
def feladat1():
    elemek = int(input("Add meg hány számot randomizáljon a program! db= "))
    szamok=[]
    for i in range(elemek):
        szamok.append(randint(1,50))

    print(szamok)
    prl=0
    for item in szamok:
        if item%2==1:
            prl= prl+1
    
    
    print(prl)

#feladat1()

def feladat2():
    elemek=int(input("Add meg mennyi számot generáljon a program:"))
    szamok=[]
    prs=0
    for i in range(elemek):
        szamok.append(randint(0,50))
    
    for item in szamok:
        if item%2==0:
            prs=prs+item
    
    print(szamok)
    print("Párosok összege:", prs)

#feladat2()

def feladat3():
    elemek=int(input("Add meg mennyi számot generáljon a program:"))
    szamok=[]
    prs=0
    for i in range(elemek):
        szamok.append(randint(0,50))
    
    for i in range(0,len(szamok)):
        if szamok[i] %2==0:
            print(szamok[i],',sorszáma:', i+1)

            




feladat3()



def alapok():
    print(lista1[1])
    print(lista1[-1]) #utolsó elem
    print(lista1[0:4])
    print(lista1[2:5])
    print(lista1[7:])
    print(lista1[:5])
    lista1[5] = 'alma'
    print(lista1)
    for item in lista1:
        print(item, end=" ")

    print()
    print(len(lista1)) #listában lévő elemek száma
    print(lista1.index('alma'))#az alma indexét megkeresi, majd kiírja
    lista1.pop()#utolsó elem eltávolítása
    print(lista1)
    lista1.remove('alma')#adott elem eltávolítása
    print(lista1)
    lista1.pop(3)
    print(lista1)
    del lista1[2]
    print(lista1)
    #lista1.clear()#törli/tiszítitotta az elemeket!
    print(lista1)
    #del lista1#TÖRLI a teljes listát!
    print(lista1)
    lista1.reverse()#fordított sorrend
    print(lista1)
    lista1.sort()#sorba rendez
    print(lista1)
    lista1.insert(3,'körte')#adott indexre tudunk beszúrni
    print(lista1)
