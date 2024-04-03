"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

lista = []
print("Seja bem vindo a sua lista de compra")
while True:
    opcao_lista = input("Voce deseja [a]adicionar, [l]listar ou [d]deletar: ").lower()
    
    if opcao_lista == "a":
        print("Digite o item")
        lista.append(input())
    elif opcao_lista == "l" and len(lista) >= 1:
        for indice, itens in enumerate(lista):
            print(indice, itens)
    elif opcao_lista == "l" and len(lista) < 1:
        print("Nao existe item para listar")
    elif opcao_lista == 'd'and len(lista) >= 1:
        print("Qual item deseja apagar, escolha o indice")
        del_i = input()
        if del_i.isdigit() and len(lista) > int(del_i):
            print("O item",lista[int(del_i)],"foi excluido")
            del lista[int(del_i)]
        else:
            print("Digite um indice existente")
    elif opcao_lista == 'd'and len(lista) <= 1:
        print("Nao existe itens na sua lista")
    else:
        print("Digite uma letra existente")
