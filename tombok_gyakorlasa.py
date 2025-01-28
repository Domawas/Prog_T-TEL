import random


lista = []

for i in range(10):
    if i % 2 == 0: 
        lista.append(1)
    else:   
        veletlen_paros = random.randint(1, 10) * 2 
        lista.append(veletlen_paros)


for elem in lista:
    print(elem)
