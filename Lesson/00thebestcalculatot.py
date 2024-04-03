def calc(digit1,digit2, conta):
    if conta == '+':
        print(digit1 + digit2)
    elif conta == '-':
        print(digit1 - digit2)
    elif conta == '*':
        print(digit1 * digit2)
    elif conta == '/': 
        print(digit1 // digit2)
    else:
        print("Digite certo pf")
while True:
    valor1 = int(input("Digite um valor:\n"))
    valor2 = int(input("Digite um valor:\n"))
    tipo_de_conta = input("Digite o tipo de conta +,-,/ ou *:\n")
    calc(valor1, valor2, tipo_de_conta )