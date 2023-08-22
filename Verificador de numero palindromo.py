#DESENVOLVIDA PARA CHECAR SE UM NUERO LIDO E TRAS PRA FRENTE É IGUAL AO NUMERO DE ENTRADA

numero = str(input("Escreva seu numero: "))
numero_vetor = list(numero)

def Inverter_string(texto):
    return texto[::-1]

if "." in numero_vetor:
    indice = numero_vetor.index(".")
    del numero_vetor[indice]
    
    numero_sem_virgula = "".join(numero_vetor)
    numero_invertido = Inverter_string(numero_sem_virgula)
else:
    numero_invertido = Inverter_string(numero)

if numero_invertido == numero:
    print(f"Esse numero é um Palindromo, o numero invertido é: {numero_invertido}")
else:
    print(f"Esse numero NAO é um Palindromo, o numero invertido é: {numero_invertido}")