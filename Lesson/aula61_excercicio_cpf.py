"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
while True:
    cpf_desconfig = input('Digite seu cpf')
    if cpf_desconfig == "":
        print("Digite um cpf valido")
    elif cpf_desconfig == False:
        print("Digite um cpf valido")   	
    else:
        try:
            cpf_list = cpf_desconfig.split(".")
            cpfend_desconf = cpf_list[2].split("-")
            cpfend= cpfend_desconf[-1]
            del cpfend_desconf[-1]
            del cpf_list[-1]
            cpf_list.extend(cpfend_desconf)
            cpf_full_str = cpf_list[0] + cpf_list[1] + cpf_list[2]
            cpf_full = int(cpf_full_str)
            contador = 10
            result_saved = []
            for results in cpf_full_str:
                digits =contador * int(results)
                contador -= 1
                result_saved.append(digits)
            totalsomado = 0
            for resulttotal in result_saved:
                totalsomado += resulttotal
            totalmod = (totalsomado * 10)%  11 
            print(totalmod)
        except IndexError:
            print("Digite o cpf com pontos e -")









"""

Primeira Tentativa


cpf_str = "746.824.890-70"
cpf_str = cpf_str.split(".")
cpfend = cpf_str[-1].split("-")
del cpf_str[-1]
cpf_str.append(cpfend[0])
cpfint1= int(cpf_str[0])
cpfint2= int(cpf_str[1])
cpfint3= int(cpf_str[2])
cpf = [cpfint1,cpfint2,cpfint3]
key_out = 0
key=0
somador = 10
saved_digit =[]
while True:
    cpf_digit = ''
    for  cpf_digit_int in enumerate(cpf[key_out[key]]):
        if key <= 3:
            cpf_digit_int *= somador
            somador -= 1
            key += 1
            saved_digit.append(cpf_digit_int)
        else:
            key == 0
            key_out +1"""
