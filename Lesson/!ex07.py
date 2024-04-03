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
print("Bem vindo ao mini game de caca palavra")
palavra = "Escola".casefold()
letra_saved = ""
tentativas = 0
while True:
    palavra_form = ""
    letra_digitada = input("Digite uma letra: \n").casefold()
    tentativas += 1
    if len(letra_digitada) == 1 and letra_digitada.isalpha():
        if letra_digitada in palavra:
            if letra_digitada not in letra_saved :
                letra_saved += letra_digitada
        for ast in palavra:
            if ast in letra_saved:
                palavra_form += ast
            else:
                palavra_form += "@"
        print(palavra_form)
        if palavra_form == palavra:
            print(f"Parabens vc ganhou com {tentativas}X")
            break
    else:
        print("Digite apenas uma letra")