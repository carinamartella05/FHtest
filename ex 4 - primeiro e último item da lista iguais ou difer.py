# verificar se o último e o primeiro item de uma lista são idênticos

lista = []

print("Digite 5 números")

for i in range(0,5):
    num = int(input())
    lista.append(num)

print(lista)

if lista[0] == lista[4]:
    print("O primeiro e último elemento da lista são idênticos")
else: 
    print("O primeiro e último elemento da lista são distintos")
