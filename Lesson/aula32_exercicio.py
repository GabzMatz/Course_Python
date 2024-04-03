"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.

numero = input("Digite um numero inteiro")
try:
    numero_divisivel = int(numero) % 2
    if  numero_divisivel == 0:
        print("Seu numero e par")
    
    else:
        print("Seu numero e impar")
except:
    print("Voce nao digitou um numero")



Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.

horario = input(f"Qual horas sao?")


try:
    horario= int(horario)
    if horario <= 11:
        print("Bom dia")
    elif horario >= 12 and horario <18:
        print("Boa tarde")
    elif horario >= 18 and horario <= 23:
        print("Boa noite")
    else:
        print("Use numeros validos")
except:
    print("Digite apenas numeros inteiros")

Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input("Digite seu nome")

try:
    quant_nome = len(nome)
    if quant_nome>0 and quant_nome <= 4:
        print("Seu nome e curto")
    elif quant_nome >= 5 and quant_nome <=6:
        print("Seu nome e normal")
    elif quant_nome >= 6 and quant_nome <= 12:
        print("Seu nome e grande")
    else:
        print("Apenas o primeiro nome pf")
except: 
    print("Digite apenas seu nome")
    