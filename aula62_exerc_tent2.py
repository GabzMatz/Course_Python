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
''''

Calculo do primeiro dígito do CPF
CPF: 746.824.890-70'''

cpf_cru = "52720963801"
cpf_novedigt = cpf_cru[:9]
contador1 = 10
digit1_saved= 0 
for digit in cpf_novedigt:
    digit1_saved += contador1 * int(digit)
    contador1 -= 1
primeiro_digito = ((digit1_saved * 10)  % 11)
primeiro_digito = primeiro_digito if primeiro_digito <= 9  else 0
print("Seu primeiro digito e:", primeiro_digito)
seg_cpf = cpf_novedigt + str(primeiro_digito)
contador2 = 11
digit2_saved= 0 
for digit2 in seg_cpf:
    digit2_saved += contador2 * int(digit2)
    contador2 -= 1 
segundo_digito = ((digit2_saved * 10)  % 11)
print("Seu segundo digito e:", segundo_digito) 
segundo_digito = segundo_digito if segundo_digito <= 9 else 0 
complet = str(cpf_novedigt)+str(primeiro_digito)+str(segundo_digito)

print(f"Seu cpf {cpf_cru} e valido") if complet == cpf_cru else print(f"Seu cpf {cpf_cru} nao e valido")