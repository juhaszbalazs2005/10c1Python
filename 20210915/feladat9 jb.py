a = int(input("Kérek egy számot! a="))
b = int(input("Kérek mégegy számot! b="))
c = int(input("Kérek egy utolsó számot! c="))

if a > b and a > c:
    print("A legnagyobb szám:", a)
elif b> a and b>c:
    print("A legnagyobb szám:", b)
elif c>b and c>a:
    print("A legnagyobb szám:", c)

if a < b and a < c:
    print("A legkisebb szám:", a)
elif b< a and b<c:
    print("A legkisebb szám:", b)
elif c<b and c<a:
    print("A legkissebb szám:", c)