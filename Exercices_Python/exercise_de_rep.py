#ele quer que eu descubra quantas vezes de uma palavra qual foi a letra que mais foi usado

palavra= input("Digite uma palavra:\n").lower()
seletor=0
letra_mais_apareceu=""
repeticoes_mais_max=0
while seletor < len(palavra):
    digit=palavra[seletor]
    if palavra == " ":
        seletor +=1
        continue
    repeticoes_mais_apareceu_round = (palavra.count(digit))
    if repeticoes_mais_apareceu_round >= repeticoes_mais_max:
        letra_mais_apareceu = digit
        repeticoes_mais_max = repeticoes_mais_apareceu_round
        seletor +=1
        continue
    seletor += 1
print("letra que mais apareceu em",palavra,"foi",letra_mais_apareceu.upper(),
      "apareceu",repeticoes_mais_max,"X")