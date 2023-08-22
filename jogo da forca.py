import os

caracters = []
espacos = []
continuar = True
vida = 6

#FUNCOES

def Limpa(): # DEF PARA LIMPAR O CONSOLE NA P/ ESCONDER A VARIAVEL{BIBLIOTECA OS}
     if os.name == 'nt': 
        _ = os.system('cls')
                 
def Desenho(quant_vida, palavra_real):
    
    if quant_vida == 6:
        print(f"____")
        print("/     ")
        print("|     ")
        print("|     ")  
        print("|     ")
        
    if quant_vida == 5:
        print(f"_____")
        print("/    O ")
        print("|      ")
        print("|      ")
        print("|      ")
        
    if quant_vida == 4:
        print(f"_____")
        print("/    O  ")
        print("|    |  ")
        print("|       ")
        print("|       ")
        
    if quant_vida == 3:
        print(f"_____")
        print("/    O  ")
        print("|   /|  ")
        print("|       ")
        print("|       ")
        
    if quant_vida == 2:
        print(f"_____")
        print("/    O  ")
        print("|   /|\ ")
        print("|       ")
        print("|       ")
        
    if quant_vida == 1:
        print(f"_____")
        print("/    O  ")
        print("|   /|\ ")
        print("|   /   ")
        print("|       ")
        
    if quant_vida == 0:
        print(f"_____")
        print("/    O  ")
        print("|   /|\ ")
        print("|   / \ ")
        print("|       ")
        print(f"\nVoce perdeu!!\nA palavra era {palavra_real}")
        return False
        
 #---------------
 
 #Comeco do pre jogo/Pegando informações
print("ESSE É O JOGO FORCA")
print("\nPeça para um seu amigo escrever a palavra para ser adivinhada")

adivinha = str(input())

for i in adivinha:
    caracters.append(i)

quantidade_caracter = len(caracters)

for i in range(quantidade_caracter):
    espaco = "_"
    espacos.append(espaco)

Limpa() 
#-------------

#Começo do jogo/Laço que o jogo esta rodando 

continuar = True
# vezes = 0

while continuar:
    vezes = 0
    print("Escreva sua letra ")
    letra = (input())



    for posicao in range(len(caracters)):
        if caracters[posicao] == letra:
            espacos[posicao] = letra
            Limpa()
            print(espacos)
            Desenho(vida, adivinha)
        else: 
            vezes = vezes+1

    if espacos == caracters:
            print("Voce ganhou !!!")
            print(f"A palavra era {adivinha}")
            continuar = False

    if vezes == len(caracters):
        vida = vida-1
        Limpa()
        print("Essa letra nao existe")
        Desenho(vida, adivinha)
        print(espacos)

        if vida == 0:
            continuar = False
   