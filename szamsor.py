
valamelyik = int(input("1: Mind kiírása.\n2:Különbözők kiírása.\nVálasztás: "))
def osszes():
    for i in range(2,5,1):
        for j in range(2,5,1):
            for k in range(2,5,1):
                print(f"{i}{j}{k}")

def kulonbozoek():
    for i in range(2,5,1):
        for j in range(2,5,1):
            for k in range(2,5,1):
                if i != j and j != k and i != k:
                    print(f"{i}{j}{k}")

if valamelyik == 1:
    osszes()
else:
    kulonbozoek()
