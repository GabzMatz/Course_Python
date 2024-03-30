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


secret_word = "fireball"
secret_ast = "********"
print("Seja bem-vindo ao mini-game")
print(len(secret_word))

letra_mem =""

while True:
    letra = input("Digite uma letra").lower()
    letra_cont = secret_word.count(letra)
    if letra in secret_word:
        print(secret_word[0])