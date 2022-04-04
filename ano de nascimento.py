
atual =  2022
mes_atual=4
dia_atual=4

while True:
    print("Indique sua idade, dia e mês de nascimento respectivamente. O programa mostrará o ano em que você nasceu")
    idade = int(input())
    mes_nascimento= int(input())
    dia_nascimento=int(input())
    
    if mes_nascimento > mes_atual:
        print(atual-idade-1)

    if mes_nascimento < mes_atual:
        print(atual-idade)

    if mes_nascimento == mes_atual:
        if dia_nascimento > dia_atual:
            print(atual-idade-1)
        if dia_nascimento < dia_atual: 
            print(atual-idade)
        if dia_nascimento == dia_atual:
            print("FELIZ ANIVERSÁRIO! Você nasceu em" , atual-idade-1) 