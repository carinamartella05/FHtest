import time
time.strftime('%Y-%m-%d', time.localtime())

ano_atual = int(time.strftime('%Y', time.localtime()))
mes_atual= int(time.strftime('%m', time.localtime()))
dia_atual= int(time.strftime('%d', time.localtime()))

while True:
    print("Indique sua idade, dia e mês de nascimento respectivamente. O programa mostrará o ano em que você nasceu")
    idade = int(input())
    dia_nascimento=int(input())
    mes_nascimento= int(input())
    
    if mes_nascimento > mes_atual:
        print(ano_atual-idade-1)

    if mes_nascimento < mes_atual:
        print(ano_atual-idade)

    if mes_nascimento == mes_atual:
        if dia_nascimento > dia_atual:
            print(ano_atual-idade-1)
        if dia_nascimento < dia_atual: 
            print(ano_atual-idade)
        if dia_nascimento == dia_atual:
            print("FELIZ ANIVERSÁRIO! Você nasceu em" , ano_atual-idade-1) 
    