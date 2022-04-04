import random
import time 

print("Tente acertar o número entre 0 e 9! Você tem 3 tentativas!")

numero = random.randint(0,9) # o computador escolhe "aleatoriamente" um número entre o intervalo mencionado
tentativas = 3 # número de tentativas que a pessoa tem para acertar o número escolhido pelo computador

while tentativas > 1:  
    hipotese = int(input()) # abre caixa de diálogo que possibilita a pessoa de chutar seu número
    if hipotese == numero:
        print("Parabéns! Você acertou")
    elif hipotese != numero:
        print("Sinto Muito, você errou! Tente novamente")
        tentativas = tentativas - 1
    
if tentativas == 1:
    hipotese = int(input()) # abre caixa de diálogo que possibilita a pessoa de chutar seu número
    if hipotese == numero:
        print("Parabéns! Você acertou")
    elif hipotese != numero:
        print("Sinto Muito, você errou!")
        tentativas = tentativas - 1

if tentativas == 0: 
        print("Suas tentativas acabaram. Jogue novamente")
        time.sleep(3)
        print("O número era ", numero)
        tentativas = 3
        

