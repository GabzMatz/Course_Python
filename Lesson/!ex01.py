
"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""


nome = input("Digite um nome:\n")
idade = input("Agora sua idade:\n")
if bool(nome) and bool(idade) == True:
    print(f"Seu nome e {nome}")
    print(f"Seu nome invertido e {nome[::-1]}")
    if " " in nome:
        espaces = nome.count(' ')
        print(f"Existe {espaces} espacos dentro de {nome}")
    print(f"Seu nome contem {len(nome)} caracteres")
    print(f"A primeira letra do seu nome e {nome[0]}")
    print(f"A ultima letra do seu nome e {nome[-1]}")

else:
    ...