#printar uma pirâmide com n linhas

linhas = int(input("Quantas linhas terá a pirâmide de asteriscos? "))
lista = []
elem_ultima = int(1 + 2 * (linhas - 1)) # 

for i in range(1, linhas+1):
    el_espec = int(1 + 2*(i - 1))
    espaços = int((elem_ultima - el_espec)/2)
    lista = []
    lista.append(espaços * " ")
    lista.append( el_espec * "*")
    print(*lista)