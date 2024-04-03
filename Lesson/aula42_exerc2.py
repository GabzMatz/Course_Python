#ele quer que eu descubra quantas vezes de uma palavra qual foi a letra que mais foi usado

print("Ola mostrarei qual caracter de alguma palavra foi mais dita")
word =input("Digite algo").lower() 




indice = 0 
quantidade_letras = 0
letra_max = ""

if " " in word:
    print(" Espacos nao sao contados como caracters")

while indice < len(word):
    letra = word[indice]
    if letra == " ":
        indice =+ 1
        continue
    
    letra_mais_apareceu = word.count(letra)
    
    if letra_mais_apareceu > quantidade_letras:
        quantidade_letras = letra_mais_apareceu
        letra_max = letra
    indice += 1
print(f"O caracter que mais apareceu foi{letra_max.upper()}Aparecendo{quantidade_letras}X ")

        

        


    
