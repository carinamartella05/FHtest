# função que substitui palavras de uma lista pelos seus inversos

def inverter_palavras():
    for palavra in palavras:
        letras = []
        for letra in palavra:
            letras.append(letra)
        letras.reverse()  
        s = ''  
        termo_concatenado = s.join(letras)
        contrario.append(termo_concatenado)

palavras = []
contrario = []
print("Digite 3 palavras")
for i in range(0,3):
    palavras.append(input())

inverter_palavras()
print(f"lista original: {palavras}\nlista com palavras invertidas: {contrario}")
