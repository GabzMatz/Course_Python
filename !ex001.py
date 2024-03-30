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



palavra_secret = "fireball"
letras_saved =""

while True:
    letra_digit = input("Digite uma letra:\n")
    palavra_form =""

    if letra_digit.isalpha() and len(letra_digit) == 1:
        if letra_digit in palavra_secret:
            
            for letra in palavra_secret:
                if letra in letra_digit or letra in letras_saved:
                    palavra_form += letra
                    letras_saved += letra
                else:
                    palavra_form += "@"
        print(palavra_form)
        if palavra_form == palavra_secret:
            print("Voce ganhou")
            break

    else:
        print("deu errado")