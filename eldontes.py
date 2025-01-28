import random
def tizenharom():
    for j in range(100): 
        szam = random.randint(10, 15)
        if szam == 13:
            return
        else:
            print(szam)

tizenharom()

def elso_tiz_paros():
    osszeg = 0
    páros_számok = 0

    for i in range(2, 21, 2):  
        osszeg += i
        páros_számok += 1
        if páros_számok == 10:  
            return osszeg

print(f"Az első 10 páros szám összeg: {elso_tiz_paros()}")


