def feladat1():
    t1 = [31,28,31,30,31,30,31,31,30,31,30,31]
    t2 = ['Január', 'Február', 'Március', 'Április', 'Május', 'Június', 'Július', 'Augusztus', 'Szeptember', 'Október', 'November', 'December']
    t3 = []
    sorszam = 0
    while sorszam < 12:
        t3.append(t2[sorszam])
        t3.append(t1[sorszam])
        sorszam = sorszam +1
    for item in t3:
        print(item, end=" ")

    #másik megoldás
    t4=[]
    cv=0
    for i in range(0,12):
        t4.append(t2[cv])
        t4.append(t1[cv])
        cv+= 1
    print(t4)

#feladat1()


def feladat2():
    t1=['első', 'második', 'utolsó']
    for item in t1:
        print(item, end=" ")

#feladat2()

def feladat3():
    t1=[1,5,32,76,43,8]
    print(max(t1))

#feladat3()

def feladat4():
    t1=[123,54,23,6,3,123,54,67]
    paros=[]
    paratlan=[]
    cv=0
    for i in t1:
        if t1[cv]%2==0:
            paros.append(t1[cv])
        else:
            paratlan.append(t1[cv])
        cv+= 1
    print("Páros számok:", paros)
    print("Páratlan számok:", paratlan)

#feladat4()

def feladat5():
    t1= ['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'JeanPierre','Sandra']
    hatk=[]
    hatn=[]
    cv = 0
    for item in t1:
        if len(item) < 6:
            hatk.append(t1[cv])
        else:
            hatn.append(t1[cv])
        cv += 1

    print(hatk)
    print(hatn)

#feladat5()




def feladat6_1():
    szo = "eltöredezettségmentesítőtlenítetthetetlenségtelenítőtlenkedhetőiteknek"
    t1=[]
    print('szó hossza:', len(szo))
    cv = 0
    for i in range(0, len(szo),5):
        if i+5<len(szo):
            t1.append(szo[i:i+5])
        else:
            t1.append(szo[i:])
    t1.reverse()
    for item in t1:
        print(item, end="")

#feladat6_1()

def feladat6_2(szoveg, karakter):
    if karakter in szoveg:
        ind=szoveg.index(karakter)
        return ind
    else:
        return -1

def feladat6_2_2():
    szov = "Juliette & Romeó"
    kar="&"
    pozicio=feladat6_2(szov, kar)
    if pozicio !=-1:
        print("A", kar, "benne van a",szov,"ben!", pozicio)
    else:
        print("A", kar, "nincs benne a", szov,"ben!")

feladat6_2_2()