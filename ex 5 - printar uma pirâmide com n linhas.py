#printar uma pirâmide com n linhas

linhas = int(input("Quantas linhas terá a pirâmide de asteriscos? ")) 
elem_ultima = int(1 + 2 * (linhas - 1)) #número de elementos da última linha 

for i in range(1, linhas+1): #loop que vai da linha 1 até a última
    el_espec = int(1 + 2*(i - 1)) #número de elementos em função da linha específica
    espaços = int((elem_ultima - el_espec)/2) #número de espaços em função da linha específica / número de elementos da linha específica
    lista = [] #linha específica
    lista.append(espaços * " ") # adiciona os espaços que a linha i (específica) terá 
    lista.append( el_espec * "*") # adiciona os asteriscos que a linha i (específica) terá 
    print(*lista) # em conjunto com o for, printa linha por linha da pirâmide, sem os colchetes e vírgulas de separação de elementos