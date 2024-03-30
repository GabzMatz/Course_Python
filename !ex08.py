"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

print("Bem vindo a sua lista de mercado")
lista_de_compra = []
while True:
    entrada = input("Deseja [A]dicionar [R]etirar ou [L]istar:\n").casefold()
    if entrada == 'a':
        lista_de_compra.append(input("Digite oq quer adicionar:\n"))
    elif entrada == "r":
        if len(lista_de_compra) == 0:
            print("Voce nao tem oq retirar")
            continue
        delet_list = input("Digite uma indice:\n")
        if delet_list.isnumeric():
            lista_de_compra.pop(int(delet_list))
        else:
            print("Digite uma indice valido!")
            pass
    elif entrada == "l":
        if len(lista_de_compra) == 0:
            print("Voce nao tem oq listar")
        for ind, iten in enumerate(lista_de_compra):
            print(ind, iten)
    elif entrada == "stop":
        break
    else:
        print("Digite uma letra valida")