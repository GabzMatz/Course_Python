def contacpf(cpf, seletor):
    digit=0
    for numero in cpf: 
        digit += seletor * int(numero)
        seletor -= 1
    digit = (digit * 10) % 11 
    digit = digit if digit <= 9 else 0
    return digit
cpfcru = input("Digite um cpf:\n").replace(".","").replace("-","")
digito1 = contacpf(cpfcru[:9], 10)
digito2 = contacpf(cpfcru[:9]+str(digito1),11)
if cpfcru == cpfcru[:9]+str(digito1)+str(digito2):
    print("Seu cpf e valido")
else:
    print("Seu cpf nao e valido")