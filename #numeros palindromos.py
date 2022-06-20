#numeros palindromos
import math 
import time

def numero_palindromo():
    for num in range(10, faixa+1):
        lista = list(str(num))
        lista_invertida = list(reversed(lista))
        numero_junto = int(''.join(lista_invertida))

        if num == numero_junto:
            palindromos.add(num)
        else:
            pass

def numero_primo():
    for i in range(2, faixa+1):
        divisores = []
        for k in range(1, i+1):
            if i%k == 0:
                divisores.append(k)
            elif i%k != 0:
                pass
        if len(divisores) == 2:
            primos.add(i)
        elif len(divisores) > 2:
            pass

def num_quadrado_pfto():
    for i in range(0, faixa +1):
        raiz = math.sqrt(i)
        if i != 0:
            decimal_raiz = float(raiz - i//raiz) 
            if decimal_raiz == 0:
                quadrados_pftos.add(i)
            else:
                pass
        if i == 0:
            quadrados_pftos.add(i)

while True:
    time.sleep(2)
    print("Considerando os números naturais... Se você quer saber quais são os números palíndromos apenas, digite 1; "
            "se o seu interesse for pelos números primos palíndromos, digite 2; e se quiser obter os números "
            "quadrados perfeitos palíndromos, digite 3")
    modo = int(input())
    faixa = int(input("Digite o número máximo que começa no 0 e contempla o número máximo: "))
    palindromos = set()
    primos = set()
    quadrados_pftos = set()

    if modo == 1:
        numero_palindromo()
        print(f"Os números palíndromos de 0 até {faixa} são: {sorted(palindromos)}")
    elif modo == 2:
        numero_palindromo()
        numero_primo()
        print(f"Os números primos palíndromos entre 0 e {faixa} são: {sorted(palindromos & primos)}")
    elif modo == 3:
        numero_palindromo()
        num_quadrado_pfto()
        print(f"Os números quadrados perfeitos palíndromos entre 0 e {faixa} são: {sorted(palindromos & quadrados_pftos)}")
    else:
        print("Essa operação não é possível")
        break