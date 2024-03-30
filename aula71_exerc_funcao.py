# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.


"""def conta(*args):
    total = 1
    for i in args:
        total *= i
    return total


sera = conta(1,2,3,4,5,6)
print(sera)
print(1*2*3*4*5*6)

"""

# funcao pra saber se e par ou impar
# 0 == False
# 1 == True
def caiu(numero):
    ngm = numero % 2
    if ngm == False:
        return f"O numero {numero} e par"
    else:
        return f"O numero {numero} e impar"
    
var = caiu(2)
print(var)