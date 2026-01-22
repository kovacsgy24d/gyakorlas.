"""import random

lista = [random.randint(0, 9) for _ in range(10)]
print("Lista:", lista)

paratlan = sum(1 for sz in lista if sz % 2 == 1)
print("Páratlanok száma:", paratlan)

egyedi = []
for sz in lista:
    if sz not in egyedi:
        egyedi.append(sz)
print("Ismétlés nélkül:", egyedi)

hiányzó = [i for i in range(10) if i not in lista]
print("Hiányzó számok:", hiányzó)"""

"""mondat ="A programozás izgalmas és kihívásokkal teli tevékenység."
szavak = mondat.split()

hosszak= []

for szo in szavak:
    hosszak.append(len(szo))

print("Szavak hossza:", hosszak)"""

"""szam = input("Adj meg egy pozitív egész számot: ")
osszeg = 0
for karakter in szam:
    osszeg += int(karakter)

print("A számjegyek összege:", osszeg)"""


"""mondat = input("Írj be egy mondatot: ")

if mondat[-1] == ".":
    print("Kijelentő mondat")
elif mondat[-1] == "?":
    print("Kérdő mondat")
elif mondat[-1] == "!":
    print("Felszólító/óhajtó mondat")
else:
    print("Nem tudom eldönteni a mondat típusát")"""


"""bemenet = input("Adj meg számokat szóközzel elválasztva: ")
szamok = [int(sz) for sz in bemenet.split()]

print("Beolvasott számok száma:", len(szamok))
print("Legnagyobb-kisebb különbség:", max(szamok) - min(szamok))

harommal = []
for sz in szamok:
    if sz % 3 == 0:
        harommal.append(sz)
print("3-mal osztható számok:", harommal)"""