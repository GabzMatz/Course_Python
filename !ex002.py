"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
print("Seja bem vindo a sua lista de compras")
compras = []
while True:
    key = input("Voce deseja [A]dicionar, [E]xcluir ou [L]istar?\n").casefold()

    if key == "a":
        compras.append(input("Digite oq deseja adicionar\n"))
    elif key == "e":
        if len(compras) == 0:
            print("Nao tem oq apagar")
        else:
            delet = input("Digite o indice para excluir\n")
            if delet.isnumeric() and  len(compras) >  int(delet):
                del compras[int(delet)]
            elif len(compras) <=  int(delet):
                print("Digite apenas numeros possiveis")
            else:
                print("Somente numeros")
    elif key == "l":
        if len(compras) == 0:
            print("Nao tem oq listar")
            continue
        else:
            for ind, itens in enumerate(compras):
                print(ind, itens)
    elif key == "break":
        break
    else:
        print("Digite um valor valido")