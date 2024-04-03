#Calculadora


print("Welcome to Calculator")
while True:
    result = 0
    welcome = input("Deseja fazer uma [C]onta ou [S]air:\n").casefold()
    if welcome == "c":
        num1 = input("Digite um valor inteiro:\n")
        num2 = input("Digite outro valor inteiro:\n")
        if num1.isnumeric() and num2.isnumeric():
            sinal = input("Qual tipo de conta deseja fazer [+] [-] [/] [*]:\n").lower()
            if sinal == "+":
                result= int(num1) + int(num2)
                print(result)
                pass
            elif sinal == "-":
                result= int(num1) - int(num2)
                print(result)
                pass
            elif sinal == "/":
                result= int(num1) // int(num2)
                print(result)
                pass
            elif sinal == "*":
                result= int(num1) * int(num2)
                print(result)
                pass
            else:
                print("Digite um sinal valido")
        else:
            print("Digite um numero valido")
            pass
    elif welcome == "s":
        print("Adeus")
        break
    else:
        print("Digite um valor valido")