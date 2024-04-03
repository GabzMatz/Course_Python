"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
while True:
    numero = input("Digite um numero:\n")

    if numero.isnumeric():
        numero_divisivel = int(numero) % 2
        print("Seu numero e par")if numero_divisivel == 0 else print("Seu numero e impar")
    elif numero == "break":
        break
    else:
        print("Digite apenas numeros inteiros pf")