"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
while True:
    cpfcru =input("Digite um cpf:\n").replace("-","") \
    .replace(".","")

    if len(cpfcru) >= 11:

        
        cpfnove = cpfcru[:9]
        seletor_num1 = 10
        seletor_num2 = 11
        digito1=0
        digito2=0
        for num1 in cpfnove:
            digito1 += int(num1)*seletor_num1
            seletor_num1 -= 1
        digito1 = (digito1 *10) % 11
        digito1 = 0 if digito1 > 9 else digito1
        cpf2 = cpfnove+str(digito1)
        for num2 in cpf2:
            digito2 += int(num2)*seletor_num2
            seletor_num2 -= 1
        digito2 = (digito2 *10) % 11
        digito2 = 0 if digito2 > 9 else digito2
        cpfnovo = cpfnove + str(digito1) + str(digito2)
        if cpfnovo == cpfcru:
            print("Seu cpf e valido")
        else:
            print("Seu cpf nao e valido")
    else:
        print("Digite apenas o cpf")