#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista 
#composta. No final, mostre um boletim contendo a média de cada um e permita que o 
#usuário possa mostrar as notas de cada aluno individualmente.

aluno = [input("Digite seu nome:\n").casefold(),input("Digite sua nota:\n"),input("Digite sua outra nota:\n")]


result_aluno = (int(aluno[1])+int(aluno[2])) / 2 

chave = input("Deseja ver sua media, e suas notas?\n").casefold()

if chave.isalnum() and "s" in chave:
    nome_aluno = input("Digite seu nome\n").casefold()
    if nome_aluno in aluno:
        print("Ok")
    print(f"{result_aluno} Suas notas foram {aluno[0]} e {aluno[1]}")
else:
    print("tmnc ent")

