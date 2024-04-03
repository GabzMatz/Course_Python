#Calculadora com While
print("Bem vindo a calculadora")
try:    
    key = None
    while True:
        if key == True:
             break
        passe = input(f"Deseja Entrar na calculadora [S]im? ")
        if passe == "S" or passe == "s":
            while True:
                        question= input("Deseja fazer uma conta de, [+], [-], [*] ou [/]?Deseja sair da calculadora Sim ou Nao? ")
                        if question == "+":
                            question_plus1=int(input(f"Fale 1 valor "))
                            question_plus2=int(input(f"Fale outro valor para somar "))
                            print(f"Sua soma deu",question_plus1 + question_plus2)
                            continue
                        if question == "-":
                            question_plus1=int(input(f"Fale 1 valor "))
                            question_plus2=int(input(f"Fale outro valor para subtrair "))
                            print(f"Sua subtracao deu",question_plus1 - question_plus2)
                            continue
                        if question == "*":
                            question_plus1=int(input(f"Fale 1 valor "))
                            question_plus2=int(input(f"Fale outro valor para multiplicar "))
                            print(f"Sua multiplicacao deu",question_plus1 * question_plus2)
                            continue
                        if question == "/":
                            question_plus1=int(input(f"Fale 1 valor "))
                            question_plus2=int(input(f"Fale outro valor para divisao "))
                            print(f"Sua divisao deu",question_plus1 // question_plus2)
                            continue
                        if question == "sim" or question == "Sim" or question == "s":
                            print("Goodbye")
                            key = True
                            break
                        else:
                            print("Digite um sinal valido")
        else:
            leave_op= input("Deseja sair do programa Sim ou Nao? ")
            if leave_op == "Sim" or leave_op == "sim" or leave_op == "s" or leave_op == "S":
                print("GoodBye")
                break
            else:
                continue
                
        
except:
    print("Adeus")





    
