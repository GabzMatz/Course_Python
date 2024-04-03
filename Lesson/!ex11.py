def conta(cpf,seletor):
    num_saved = 0
    for numero in cpf:
        num_saved += int(numero) *seletor
        seletor -= 1
    digito = (num_saved *10) %11
    digito = digito if digito <= 9 else 0
    return digito
cpfreal = input('Digite seu cpf:\n').replace(".","").replace("-","")
digit1 = conta(cpfreal[:9], 10)
cpf2 = cpfreal[:9]+ str(digit1)
digit2 = conta(cpf2, 11)
if cpfreal == cpf2 + str(digit2):
    print("Este cpf e Valido")
    print(digit1)
    print(digit2)
else:
    print("este cpf nao e valido")