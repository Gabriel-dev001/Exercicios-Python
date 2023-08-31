import random 
import os

continuar = False

def Limpa(): # DEF PARA LIMPAR O CONSOLE NA P/ ESCONDER A VARIAVEL{BIBLIOTECA OS}
     if os.name == 'nt': 
        _ = os.system('cls')

def Dicas (numero, num_atual):
    if numero%2 == 0:
        primeira_dica = "O numero a ser adivinhado é par"

    if numero%2 == 1:
        primeira_dica = "O numero a ser adivinhado é impar"

    if num_atual<numero:
        segunda_dica = "O numero a ser adivinhado é maior"

    if num_atual>numero:
        segunda_dica = "O numero a ser adivinhado é menor"

    qual_dica = random.randint(1, 2)

    if qual_dica == 1:
        print(primeira_dica)

    if qual_dica == 2:
        print(segunda_dica)

    
print ("Qual a sua dificuldade que voce quer jogar")
print("  1 - EASY")
print("  2 - MEDIUM")
print("  3 - HARD")

dificuldade = int(input())

while dificuldade<1 or dificuldade>3:
    Limpa()
    print ("Qual a sua dificuldade que voce quer jogar")
    print("  1 - EASY")
    print("  2 - MEDIUM")
    print("  3 - HARD")

    dificuldade = int(input())

match(dificuldade):
    case 1:
        num_max = 10
        tentativas = 11

    case 2:
        num_max = 50
        tentativas = 21
        

    case 3:
        num_max = 100
        tentativas = 11

numero_sorteado = random.randint(1, num_max) 

while num_max !=0 :
    tentativas = tentativas-1
    chutador = 0
    print(f"Voce tem {tentativas} tentativas")
    Dicas(numero_sorteado, chutador)
    print("   Chute um numero:")
    chutador = int(input())
    Limpa()

    if tentativas == 0: 
        print("Voce perdeu !!!")
        print(f"O numero era {numero_sorteado}")
        break
    
    if chutador == numero_sorteado:
        print("Voce adivinhou o numero :) !!!")
        print(f"O numero era {numero_sorteado}")
        break

    if chutador != numero_sorteado:
        print("Que pena! Voce errou...\n")