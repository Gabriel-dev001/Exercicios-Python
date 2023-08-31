# INVERTER PALAVRA

palavra = str(input())
caracters = []
invertido = []
substituirs = []
cont = 0

for i in palavra:
     caracters.append(i)

quantidade = len(caracters)

for i in range(quantidade):

    while cont < quantidade :
        quantidade = quantidade - 1
        substituir = caracters[quantidade]
        substituirs.append(substituir)
    

print(substituirs) 