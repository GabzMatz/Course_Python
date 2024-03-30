#Faca um prgrama que mostre qual letra mais apareceu

#Forma de laco for
"""
palavra = input("Digite uma palavra:\n").casefold()
letra_saved = ""
letramax = 0
for letra in palavra:
    letramax_round = palavra.count(letra)
    letra_saved_round = letra
    if letramax_round > letramax:
        letra_saved = letra_saved_round
        letramax = letramax_round
print(f"A letra que mais apareceu na palavra {palavra.upper()} foi \
{letra_saved.upper()} aparecendo {letramax}x") 
"""
#Forma de laco while

palavra = input("Digite uma palavra:\n").casefold()
seletor = 0
letra_saved = ""
letramax = 0
while len(palavra) > seletor:
    letra = palavra[seletor]               
    contador_letra =palavra.count(letra)
    if letramax < contador_letra:
        letra_saved = letra
        letramax = contador_letra
    seletor += 1
print(f"A letra que mais apareceu na palavra {palavra.upper()} foi \
{letra_saved.upper()} aparecendo {letramax}x") 
