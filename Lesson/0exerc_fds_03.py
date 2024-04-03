#Faca um programa que mostre quanta vezes a letra mais vista aparece


print("Ola seja bem vindo")
seletor = 0
letra_max = ''
letra_mais_apareceu = 0
palavra = input("Digite uma palavra:\n").lower()
while True:
    if seletor == len(palavra):
        print("A letra que mais apareceu na palavra", palavra,"\n",letra_max,"aparecendo",letra_mais_apareceu)
        break
    
    if " " in palavra:
        seletor += 1
    if bool(palavra) == True:
        while seletor < len(palavra):
            letra = palavra[seletor]
            letra_mais_apareceu_round = palavra.count(letra)
            if letra_mais_apareceu_round > letra_mais_apareceu:
                letra_mais_apareceu = letra_mais_apareceu_round
                letra_max = letra
                seletor +=1
                continue
            seletor +=1
    else:
        ...