# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def numero_multiplicador(numero_digit_mult):
    def multipicador(numero):
        return numero * numero_digit_mult
    return multipicador

duplicar = numero_multiplicador(2)
triplicar = numero_multiplicador(3)
quadriplicar = numero_multiplicador(4)

print(duplicar(int(input("Digite um numero"))))
print(triplicar(3))