def executa(funcao, *args):
    return funcao(*args)


print(executa(lambda x, y: x+y ,2,3 ))
teste = executa(lambda n1 , n2: n1 + n2, 2, 3)
print(teste)
"""teste2 = lambda n1 , n2: n1 + n2, 2, 3
print(executa(teste2))"""



#teste dict

"""v1 = {
"nome" : "joao",

}
v1.setdefault("nome2","Zeca")
print(v1)"""