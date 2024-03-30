# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opcoes': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opcoes': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opcoes': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
def quiz(lista):
    acertos = 0
    print(perguntas[lista]["Pergunta"])
    for i, opcao in enumerate(perguntas[lista]["Opcoes"]):
        print(f"{i}) {opcao}")
    result=input("Escolha uma opçao!\n")
    if result == perguntas[lista]["Resposta"]:

        print("Voce acertou")
        acertos += 1
        return acertos
    else:
        print("mamou")
        return acertos
input("Ola seja bem vindo ao nosso quiz, irei fazer 3 perguntas vms la?\n")
quiz_1 = quiz(0)
quiz_2 = quiz(1)
quiz_3 = quiz(2)
print(f"Voce {int(quiz_1+quiz_2+quiz_3)}X acertos de 3 perguntas")