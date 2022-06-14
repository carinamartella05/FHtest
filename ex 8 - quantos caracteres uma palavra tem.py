#programa que conta quantos caracteres uma palavra tem

word = str(input("Digite uma palavra: "))
lista = list(word)
print(f"A palavra {word} tem {len(word)} caracteres")

# OU (usando a ferramenta de loop)

i = 0
for letra in word:
    i +=1
print(f"A palavra {word} tem {i} caracteres")

