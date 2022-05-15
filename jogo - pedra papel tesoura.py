# pedra, papel e tesoura

import random as rd
import time
opções = ["pedra", "papel", "tesoura"]


while True:
    print("PEDRA, PAPEL OU TESOURAAA!!")
    pc = rd.choice(opções)
    time.sleep(3)
    jogador = input()
    if jogador == pc:
        print("O jogo está empatado!")
    elif jogador == 'pedra' and pc == 'papel':
        print("pc ganhou!")
    elif jogador == "pedra" and pc == "tesoura":
        print("jogador ganhou!")
    elif jogador == "tesoura" and pc == "pedra":
        print("pc ganhou!")
    elif jogador == "tesoura" and pc == "papel":
        print("jogador ganhou!")
    elif  jogador == "papel" and pc == "pedra":
        print("jogador ganhou")
    elif jogador == "papel" and pc == "tesoura":
        print("pc ganhou")
    
    print ("Queres jogar novamente?")
    resposta = input()
    if resposta == 'sim':
        continue
    else: 
        break