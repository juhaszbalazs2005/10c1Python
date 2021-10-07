"""
#11. Írasd ki a számokat -30 és 30 között ötösével (-30, -25, -20…)! 

for i in range(-30,31,5):
    print(i, end=" ")
"""
#12. Írasd ki a 3 első tizenhét többszörösét! (3, 6, 9..) 



"""
#13. Írasd ki 2 első tizenhat pozitív egész kitevőjű hatványát (2, 4, 8, 16, 32,…)

for i in range(1,16):
    print(pow(2,i), end=' ')
print()
for i in range(1,17):
    print("2 a(z)",i,"hatványon:", pow(2,i))
print()
"""
#14. Írasd ki a 7-es szorzótábla első 25 eleméből azokat, amik 4-gyel oszthatók. 



#15. Írasd ki a 144 osztóit! 



#16. Írj programot, mely beolvas egy pozitív egész számot, és kiírja az osztóit! 


"""
#17. Írj programot, mely beolvas egy pozitív egész számot, és kiírja az osztóinak az összegét! 

a = int(input("Kérek egy pozitív egész számot! a="))
osszeg = 0

for i in range(1,a+1):
    if a%i==0:
        osszeg+=i
print("A(z)", a, "osztóinak összege:", osszeg,".")
"""

#18. Írasd ki azokat a kétjegyű számokat, amelyek számjegyeinek összege 10 (19 28 37 ...) 



#19. Írasd ki azokat a számpárokat, amelyek összege 18 (1 -17, 2 -16, …) 



#20. Írasd ki a nyolcas szorzótábla első tíz tagját egymás mellé!

for i in range(8,81):
    if i%8==0:
        print(i, end=" ")

