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

palavra_secreta = "Espelho".lower()
print("Welcome the mini-game for python")
letra_salvas=""
while True:
    

    letra_pedida=input("Digite uma palavra: ").lower()
    
    if len(letra_pedida) > 2:
        print("Digite apenas uma palavra")
        continue
    
    else:
        
        if letra_pedida in palavra_secreta:
            letra_salvas += letra_pedida
            

            palavra_formando=""
            for letra in palavra_secreta:
                if letra in letra_salvas :
                    palavra_formando += letra
                else:
                    palavra_formando += "*"
            print(palavra_formando)
            if palavra_formando == palavra_secreta:
                print("Parabens voce ganhou o game")
                print("A palavra secreta era",palavra_secreta)
                break
        else:
            print("nao contem a letra",letra_pedida )
