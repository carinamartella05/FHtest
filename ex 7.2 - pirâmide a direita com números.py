#pirâmide a direita com numeros 

num = int(input("Qual o número máximo na pirâmide unilateral de números? "))

for i in range(1, num +1):
    lista = []
    for j in range(1,i+1):
        lista.append(i)
    print(*lista)