import random
import math


def osszead(a, b):
    return a + b  

def kiirKonzolra(szoveg):
    print(szoveg)  


def f1_Elso10SzamOsszege():
    eredmeny = sum(range(1, 11)) 
    kiirKonzolra(f"Az első 10 szám összegének eredménye: {eredmeny}")
    return eredmeny


def f2_KettoSzamOsszegeKiirva(a, b):
    eredmeny = osszead(a, b)  
    kiirKonzolra(f"A két szám ({a} és {b}) összege: {eredmeny}")


def f3_NegySzamOsszegeKiirva(a, b, c, d):
    eredmeny = osszead(osszead(a, b), osszead(c, d)) 
    kiirKonzolra(f"A négy szám ({a}, {b}, {c}, {d}) összege: {eredmeny}")


def f4_HaromSzamOsszegenekGyokeKiirva(a, b, c):
    eredmeny = osszead(osszead(a, b), c)
    gyok = math.sqrt(eredmeny) 
    kiirKonzolra(f"A három szám ({a}, {b}, {c}) összege: {eredmeny}, a négyzetgyöke: {gyok}")


f1_Elso10SzamOsszege() 

f2_KettoSzamOsszegeKiirva(3, 7) 

f3_NegySzamOsszegeKiirva(1, 2, 3, 4) 

f4_HaromSzamOsszegenekGyokeKiirva(4, 5, 6)  
