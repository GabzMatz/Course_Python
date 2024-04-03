#teste de calculadora usando so funcoes
def conta(tipo,digit1= 0,digit2 = 0):
    if tipo == "Adicao" or tipo == "a":
        total = digit1 + digit2
    elif tipo == "Subtracao" or tipo == "s":
        total = digit1 - digit2
    elif tipo == "Multiplicacao" or tipo == "m":
        total = digit1 - digit2
    elif tipo == "Divisao" or tipo == 'd':
        total = digit1 - digit2
    elif tipo == "Potenciacao" or tipo == "p":
        def potenciacao(numero):
            total = digit1 ** numero
            return total
        return potenciacao
    else:
        print("Digite um numero Valido")
    return total
questionWelcome=input("Ola seja bem vindo a calculadora deseja fazer conta [S]im, [N]ao:\n").casefold()
key= 0
if questionWelcome == "s":
    while True:
        pergunta = input("Deseja fazer uma conta de [D]ivisao, [M]ultiplicacao, [A]dicao , \
[S]ubtracao ou deseja fazer um [p]otenciacao:\n").casefold()
        if pergunta == "p" or pergunta == "Potenciacao":
            valor_potencia = int(input("qual numero deseja fazer a potencia\n"))
            digit1 = int(input("Fale um numero:\n"))
            funcaopotencia = conta(pergunta,(valor_potencia))
            print(funcaopotencia(digit1))
            continue
        while key == 0:
            try:
                digit1 = int(input("Fale um numero:\n"))
                digit2 = int(input("Fale outro numero:\n"))
                key += 1
            except:
                print("Digite apenas numeros")
        valor = conta(pergunta, digit1, digit2 )
        print(f"O valor e {valor}")
        key -= 1