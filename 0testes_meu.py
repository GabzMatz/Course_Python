"""nome ="Gabriel Matos Antiqueira"
idade = 20
maior_de_idade = idade >= 18

if maior_de_idade:
    print("voce nao pode entrar aqui")
else:
    print("voce pode")




a="opa"
b=12345
c= 0.85

txt= "a={2} b={1} c={0}"
txt_comp = txt.format(a, b ,c)
print(txt_comp)

"""
#Todos os tipos de "LISTAS" em python
"""test1 = [1,2,3,4]
test2 = 1,2,3,4
test3 = {1,2,3,4}
test4 = {"numero1": 1, "numero2":2}
print(type(test1),type(test2),type(test3),type(test4))

"""



numeros = [1,2,3,4,5]

novos_numeros = [numero for numero in numeros if numero > 2]
print(novos_numeros)