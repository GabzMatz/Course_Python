entrada = input("[E]ntrar [S]air")
senha = input("Digite sua senha")


if entrada =="E" or entrada =="e" and senha == "123456":
    print("Voce esta conectado")
    
elif entrada =="S" or entrada =="s":
    saida = input("realmente deseja sair?")
    if saida=="s" or saida=="S":
        print("voce saiu do sistema")
    else:
        print("voce retornou ao lobby")
else:
    print("adeus mano")