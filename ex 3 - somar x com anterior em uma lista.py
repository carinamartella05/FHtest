#lista com 10 elementos - somar x com seu anterior - 10 somas 

print("Digite 10 números que vão compor uma lista: ")
lista = []
for i in range(10):
    num = int(input()) #usuário escreve um num
    lista.append(num) # num é adicionado na lista "lista"
print(f"Sua lista é: {lista}")

anterior = 0
atual = lista[0] #atual é inicialmente o primeiro elemento da lista
soma = anterior + atual 
print(f"A soma do 1° elemento com o elemento anterior inexistente é: {soma}") # soma o primeiro elemento da lista com o "nada"

for k in range(10): #de 0 ao 9 e não de 1 ao 10, pois são os índices dos elementos da lista
    index = k +1 # o elemento a ser utilizado será o de índice k +1
    anterior = atual 
    atual = lista[index]
    soma = anterior + atual
    print(f"A soma do {k+1}° com o {k +2}° elemento é: {soma}")