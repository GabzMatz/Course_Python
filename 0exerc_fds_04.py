"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""




palavra_secret = "dorama"
letra_acertada = ""
quant_de_letra = 0


print("Welcome to the game")


while True:
    palavra_formando =""
    letra = input("Digite uma letra:\n").casefold()


    if len(letra) > 1:
        print("Digite apenas uma letra") 
        quant_de_letra +=1
        continue
    if len(letra) == 1 and letra.isalpha():
        if letra in palavra_secret:
            letra_acertada += letra
            for ast in palavra_secret:
                if ast in letra_acertada:
                    palavra_formando += ast
                if ast not in letra_acertada:
                    palavra_formando += "@"
        if palavra_formando == palavra_secret:
            print("Voce ganhou, a palavra era:\n",palavra_formando,"\nVoce achou em",quant_de_letra,"tentativas")
            break
        print(palavra_formando)
        
    if letra.isnumeric():
        print("Somente letras pf")



