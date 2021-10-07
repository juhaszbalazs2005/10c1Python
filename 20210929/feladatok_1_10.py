# Írasd ki a számokat 1-től 20-ig! 
#a. egymás mellé 
"""
for i in range(1,21):
    print(i, end=" ")
"""
"""
print()
#b. egymás alá
for i in range(1,21):
    print(i)
"""
"""
#írasd ki a számokat ciklussal 15-92-ig egymás mellé! 
for i in range(15,93):
    print(i, end=" ")
"""
"""
#Írasd ki a páros számokat 1 és 30 között! 
#a. egymás mellé 
for i in range(1,31):
    if i%2==0:
        print(i, end=" ")
"""
"""
#b. egymás alá
for i in range(1,31):
    if i%2==0:
        print(i)
"""
"""
# Írj programot, mely beolvas egy pozitív egész számot, és kiírja az egész számokat a 
#képernyőre eddig a számig, egymástól szóközzel elválasztva! 
a = int(input("Adj meg egy egész számot! a="))
for i in range(1,a+1):
    print(i, end=" ")
"""
"""
#Írj programot, mely beolvas egy pozitív egész számot, és kiírja az egész számokat egymás 
#alá a képernyőre eddig a számig! 
a = int(input("Adj meg egy számot! a="))
for i in range(a+1):
    print(i)
"""
"""
#Írasd ki az első tizenöt szám négyzetét! 
for i in range(1,16):
    print(i * i, end=" ")
"""
"""
#Írasd ki a 4-el osztható számokat 100 és 400 között!
for i in range(100,401):
    if i%4==0:
        print(i, end=" ")
"""
"""
#Írasd ki a számokat 30 és 100 között kilencesével (30, 39, 48…)!
for i in range(30,101,9):
    print(i, end=" ")
"""
"""
#Írasd ki a számokat 150 és 40 között tizenkettesével lefelé (150, 138, 126…)! 
for i in range(150,39,-12):
    print(i, end=" ")
"""
"""
#Írasd ki 100-tól visszafelé -100-ig a kilenccel osztható számokat! 
for i in range(100,-101,-1):
    print(i, end=" ")
"""

"""
# Írasd ki a számokat 1-től 20-ig! 
#a. egymás mellé
i=1
while i<21:
    print(i, end=" ")
    i=i+1
print()
"""
"""
#b egymás alá
i=1
while i<21:
    print(i)
    i=i+1
print()
"""
"""
# Írasd ki a számokat ciklussal 15-92-ig egymás mellé! 
i=15
while i<93:
    print(i, end=" ")
    i=i+1
"""
"""
#Írasd ki a páros számokat 1 és 30 között!
#egymás mellé
i=1
while i<31:
    i=i+1
    if i%2==0:
        print(i,end=" ")
"""
"""
#egymás alá
i=1
while i<31:
    i=i+1
    if i%2==0:
        print(i)
"""
"""
#Írj programot, mely beolvas egy pozitív egész számot, és kiírja az egész számokat a 
#képernyőre eddig a számig, egymástól szóközzel elválasztva!
i=int(input("Adj meg egy számot!"))
a=1
while a<i:
    print(a, end=" ")
    a=a+1
"""
# 
