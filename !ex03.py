"""
1        Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
while True:
    horas = input("Digite qual horas sao:\n")

    if horas.isnumeric():
        if int(horas) <= 11:
            print("Bomdia")
        elif int(horas) <= 17:
            print("Boatarde")
        elif int(horas) <= 24:
            print("Bonoite")
    else:
        print("Digite apenas horas")

2          Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input("Digite seu nome\n")
if len(nome) <= 4:
    print("Seu nome é curto")
elif len(nome) <= 7:
    print("Seu nome é normal")
elif len(nome) >  7:
    print("Seu nome é muito grande")