digito = 0
def conta_cpf(cpf, seletor):
    global digito 
    num_saved = 0
    for numero in cpf:
        
        num_saved += int(numero)*seletor
        seletor -= 1
    digito += (num_saved * 10) % 11
    digito = digito if digito <= 9 else 0
cpf= "18400867858".replace(".","").replace("-","")
conta_cpf(cpf[:9], 10)
digito1 = digito
cpf2 = cpf[:9] + str(digito1)
digito = 0
conta_cpf(cpf2, 11)
digito2 = digito
if cpf[:9]+str(digito1)+str(digito) == cpf:
    print("Seu cpf e valido")
else:
    print("Cpf nao e valido")