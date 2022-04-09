import time

usuario_salvo = [str("cavalodetroia_69") , str("schr_divine" )] # usuários previamente salvos 
senha_salva = [str("domingaodofaustao") , str("uaimai" )] # senhas previamente salvas
nao_possui = str("inexistente")
u = 1 # variável determinante de um loop

while u == 1: 
    print("Insira seu usuário! Se você não possui um, digite inexistente")
    usuario_teste = str(input()) # pessoa insere seu usuário

    while usuario_teste in usuario_salvo:  
        senha_teste = str(input("Insira sua senha: ")) # pessoa insere sua senha
        indice = usuario_salvo.index(usuario_teste)
        if senha_teste == senha_salva[indice]:
            print("Olá, você está conectado!")
            u = 0 # quebra do loop - o programa cessa
            break # quebra do loop interno
        elif senha_teste != senha_salva[indice]:
            print("Senha incorreta! Tente novamente")

    if usuario_teste not in usuario_salvo and usuario_teste != nao_possui:
        print("Este usuário não existe")

    if usuario_teste == nao_possui:
        print("Vamos criar um usuário então, e posteriormente uma senha")
        time.sleep(2)
        usuario_novo = str(input("Crie seu nome de usuário: ")) # pessoa cria um usuário novo
        while usuario_novo in usuario_salvo:
            print("Este usuário já existe. Seu nome deve ser autêntico! Insira novamente")
            usuario_novo = str(input())
        if usuario_novo != usuario_salvo:
            print("Usuário criado com sucesso")
            time.sleep(2)
            senha_nova = str(input("Agora crie sua senha: ")) # pessoa cria uma senha nova
            print("Prontinho! Agora realize seu login")
            usuario_salvo.append(usuario_novo) # usuário novo é salvo na lista como último elemento dela
            senha_salva.append(senha_nova) # senha nova é salva na lista como último elemento dela
            print(usuario_salvo) 
            print(senha_salva)

if u ==0:
    time.sleep(2)
    print("Bem-vindo novamente!")
