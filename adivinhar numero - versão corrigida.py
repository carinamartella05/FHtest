import random
import time

print("Tente acertar o número entre 0 e 9! Você tem 3 tentativas!")

numero = random.randint(0,9) # o computador escolhe "aleatoriamente" um número entre o intervalo mencionado
tentativas = 3 # número de tentativas que a pessoa tem para acertar o número escolhido pelo computador


while True: #loop forever
    hipotese = int(input()) # abre caixa de diálogo que possibilita a pessoa de chutar seu númeroif tentativas >=1:  
    if hipotese == numero:
        print("Parabéns! Você acertou")
        break
    elif hipotese != numero:
        print("Sinto Muito, você errou! Tente novamente")
        tentativas = tentativas - 1
    if tentativas == 0: 
        print("Suas tentativas acabaram. Jogue novamente")
        time.sleep(2)
        print("O número misterioso era " , numero)
        tentativas = 3
        break
        
