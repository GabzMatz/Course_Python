nome =input("Digite seu nome:")
idade =input("Digite sua idade:")



if bool(nome) == True and bool(idade) == True:
    print(f"seu nome: {nome}")
    print(f"Seu nome invertido ficaria: {nome[::-1]}")
    print(f"Seu nome contem: {len(nome)} caracteres")
    print(f"O primeira letra do seu nome é: {nome[0]}")
    print(f"O ultima letra do seu nome é: {nome[-1]}")
    if " " in nome:
       print("seu nome contem espaços")
    else:
      print("nao contem espaços no seu nome")  
    
else:
    print("Desculpe voce deixou algum campo vazio")
    