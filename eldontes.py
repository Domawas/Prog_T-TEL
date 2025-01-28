import random
def tizenharom():
    for j in range(100): 
        szam = random.randint(10, 15)
        if szam == 13:
            return
        else:
            print(szam)

tizenharom()


def elso_tiz_párosok_osszege():
    osszeg = 0
    for i in range(1, 11): 
        if i % 2 == 0: 
            osszeg += i
    return osszeg


print(f"Az első 10 szám párosainak összeg: {elso_tiz_párosok_osszege()}")


def elso_38_paratlan():
    osszeg = 0
    szam = 24 
    for _ in range(38):
        osszeg += szam
        szam += 2  
    return osszeg


print(f"Az első 38 páratlan szám összege 24-től kezdve: {elso_38_paratlan()}")


def abszolut_ertek():
    for i in range(3, -4, -1):
        if i < 0:
            print(f"|{i}| = {-i}")
        else:
            print(f"|{i}| = {i}")


abszolut_ertek() 
