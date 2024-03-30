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


print("Hello, this is my game, the secret word")
palavra_secreta = "Arroz"
palavra_formando =""
letra_saved=""

while True:
    letra_input = input("Digite uma letra: ").lower()
    
    
    if letra_input in palavra_secreta.lower():
        letra_saved += letra_input
        for ast in palavra_secreta.lower():
            if ast in letra_saved:
                palavra_formando += ast
            else:
                palavra_formando += "*"
    else: 
        print("Nao temos esta palavra")
    print(palavra_formando)       
    palavra_formando =""