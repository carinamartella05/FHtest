

seq = [1,1]
inicial = 1
atual = 1
soma = inicial + atual 

num_max = int(input("Qual será o número máximo visualizado na sequência? "))

if num_max != 0:
    while soma <= num_max:
        seq.append(soma)
        inicial = atual 
        atual = soma 
        soma = inicial + atual
    else:
        print(seq)
if num_max == 0:
    seq = []
    print(seq)


    

    