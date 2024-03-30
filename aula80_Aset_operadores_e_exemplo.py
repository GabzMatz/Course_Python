# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2 # une os dois sets
s3 = s1 & s2 # une apenas os iguas
s3 = s2 - s1 # mostra apenas o valor diferente do lado esquerdo no caso 2 e 3
s3 = s1 ^ s2 # pega os valores diferente de ambos
#print(s3)


# Exemplo de uso dos sets
letras = set()
while True:
    letra = input('Digite: ')
    letras.add(letra.lower())

    if 'l' in letras:
        print('PARABÉNS')
        break

    print(letras)