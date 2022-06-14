#printar algo ao inverso

num = input("Insira um número com mais de 5 dígitos e ele será invertido: ")
lista = []
for i in num:
    lista.append(i)
lista.reverse()

print(*lista, sep='')