#Calculadora
print("Welcome")
re_op_key = 0
while re_op_key == 0:
    opening = input("Deseja entrar [S]im ou [N]ao:\n").lower()
    if opening.isalpha() and "s" in opening:
        print("Ok")
        while re_op_key == 0:
            result = 0
            numberone = input("Digite o primeiro valor para sua operacao\n")
            numbertwo = input("Digite o segundo valor para sua operacao\n")
            if numberone.isnumeric() and numbertwo.isnumeric():
                print("Voce quer qual tipo de conta")
                type_conta = input("[+]Adicao,[-]Subtracao,[*]Multiplicacao,[/]Divisao\n")
                if type_conta == "+":
                    result = int(numberone) + int(numbertwo)
                elif type_conta == "-":
                    result = int(numberone) - int(numbertwo)
                elif type_conta == "*":
                    result = int(numberone) * int(numbertwo)
                elif type_conta == "/":
                    result = int(numberone) // int(numbertwo)
                else:
                    print("Digite apenas o sinal aritmetico ")
                    continue
                print("Seu resultado e:\n",result)
                while True:
                    re_opening = input("Deseja fazer outra conta[S]im ou [N]ao").lower()
                    if re_opening == "s":
                        break
                    elif re_opening == "n":
                        print("Adeus")
                        re_op_key = 1
                        break
                    else:
                        print("Digite apenas s or n")
            else:
                print("Digite apenas numeros")
        else:
            break
    elif opening.isalpha()and "n" in opening:
        print("Goodbye")
        break
    else:
        print("Digite um S or N")