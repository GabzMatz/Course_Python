print("Sua Lista de Compra com Python")
key= 0
lista = []
while True:
    resul = input(f"Selecione uma opção:\n[i]nserir, [a]pagar, [l]ista\n").lower()

    if resul == "i":
        valor= input("Digite um valor\n")
        lista.append(valor)
        key +=1
        continue 
    elif resul == "l" and key > 0:
        print("Sua lista:")
        for ind, valore in enumerate(lista):
            print(ind, valore)
        continue
    elif resul == "l" and key < 0:
        print("Nao existe lista")
        continue
    elif resul == "a" and key > 0: 
        while True:
            try:
                apagnum = int(input("Qual Indice deseja apagar\n"))
                if apagnum in range(len(lista)):
                    del lista[apagnum]
                    key -= 1
                    break
            except:
                print("Digite um numero valido")
    elif resul == "a" and key < 0: 
        print("Nao existe item para apagar")
        continue
    else:
        print("Use uma dessas opcoes")