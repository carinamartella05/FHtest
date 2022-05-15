import math
import time

g = 10 

print("Instruções:"
        "O objetivo do jogo é acertar uma flecha no seu oponente, localizado a uma distância x" '\n'
        "Considere que os jogadores são tidos como pontos no chão, tendo altura nula" '\n'
        "E que as flechas são lançadas do chão também" '\n'
        "Ademais, uma tolerância de meio metro atrás e a frente do oponente é considerada. " 
        "Então, se por exemplo o jogador estiver na posição 5, e o atirador tiver um alcance" 
        " de 4,5 ou 5,5 m, ele terá acertado o oponente" '\n'
        "Lembrando que a flecha realiza um movimento oblíquo, e neste modo, resistências do ar são desprezadas")
time.sleep(10)

u = 1
distancia = float(input('Qual a distância inicial dos jogadores, em metros? Quanto maior for a distância, ' 
                        "maior o grau de dificuldade do jogo" '\n'))
print("Vez do jogador 1")

while u == 1:
    jogador1 = 1
    jogador2 = 0
    
    while jogador1 == 1 and jogador2 == 0:
        vel = float(input("Qual a velocidade incial de lançamento da sua flecha em m/s? "))
        ang = int(input("Qual ângulo você deseja lançar a flecha? Escolha um valor entre 0 e 90° "))

        radiano = float(ang * math.pi) / 180
        alcance = float(vel * vel * math.sin( 2 * radiano)/ g)
        
        #print(alcance)
        if alcance >= distancia - 0.5 and alcance <= distancia + 0.5:
            print("Jogador 1 ganhou!" '\n'
                    f"Você acertou seu oponente com uma margem de erro de {math.fabs(alcance - distancia)} metros")
            input("Você deseja jogar novamente? ")
            if input() == 'sim':
                u = 1
                distancia = float(input('Qual a distância inicial dos jogadores, em metros? Quanto maior for a distância, ' 
                        "maior o grau de dificuldade do jogo" '\n'))
            elif input() == 'não':
                u = 0
                break
        else:
            print("Jogador 1 errou! Vez do jogador 2")
            jogador1 = 0
            jogador2 = 1
            
    while jogador2 == 1 and jogador1 == 0:
        vel = float(input("Qual a velocidade incial de lançamento da sua flecha? "))
        ang = int(input("Qual ângulo você deseja lançar a flecha? Escolha um valor entre 0 e 90° "))

        radiano = float(ang * math.pi) / 180
        alcance = float(vel * vel * math.sin( 2 * radiano)/ g)
        #print(alcance)

        if alcance >= distancia - 0.5 and alcance <= distancia + 0.5:
            print("Jogador 2 ganhou!" '\n'
                    f"Você acertou seu oponente com uma margem de erro de {math.fabs(alcance - distancia)} metros")
            input("Você deseja jogar novamente? ")
            if input() == 'sim':
                u = 1
                distancia = float(input('Qual a distância inicial dos jogadores, em metros? Quanto maior for a distância, ' 
                        "maior o grau de dificuldade do jogo" '\n'))
            elif input() == 'não':
                u = 0
                break
        else:
            print("Jogador 2 errou! Vez do jogador 1")
            jogador1=1
            jogador2 = 0

while u == 0:
   break
        


