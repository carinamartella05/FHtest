# números primos

faixa = int(input("Digite um número máximo para o intervalo de números que começa no 0 e contempla o número máximo: "))
if faixa == 1 or faixa == 0:
    print("Não há números primos nesse intervalo")
else:
    primos = []
    for i in range(2, faixa+1):
        divisores = []
        for k in range(1, i+1):
            if i%k == 0:
                divisores.append(k)
            elif i%k != 0:
                pass
        if len(divisores) == 2:
            primos.append(i)
        elif len(divisores) > 2:
            pass

    print(f"Números primos no intervalo de 0 até {faixa}: \n {primos}")