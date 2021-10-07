# Írj programot, mely beolvas két egész számot, és kiírja a képernyőre a nagyobbat!
a = int(input("Adj meg egy számot! a="))
b = int(input("Adj meg egy másik számot! b="))
if a > b:
    print("A nagyobbik szám:", a)
elif a == b:
    print("A két szám egyenlő!")
else:
    print("A nagyobbik szám:", b)
print("     ")
if a != b:
    print("A nagyobb szám:", max(a, b))
else:
    print("A két szám egyenlő!")
