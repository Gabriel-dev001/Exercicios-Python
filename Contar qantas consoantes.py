# CONTAR QUANTAS CONSOANTES EM UMA CADEIA

palavra = str(input())
caracters_certo = []
vogais = 0
consoantes = 0
continuar = True

for i in palavra:
    caracters_certo.append(i)

quantidade = len(caracters_certo)

for i in range(len(caracters_certo)):
    if caracters_certo[i] == 'a' or caracters_certo[i] == 'e' or caracters_certo[i] == 'i' or caracters_certo[i] == 'o' or caracters_certo[i] =='u':
        vogais = vogais+1

    else:
        consoantes = consoantes+1

print(f"Existe {vogais} vogais e { consoantes } consoantes")
print(caracters_certo)
