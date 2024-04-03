# Modulos sao singletowns ou seja eles so tem uma vem uma vez pro codigo

# O importLib reload o modulo
import importlib



import aula98_m

print(aula98_m.variavel)

for i in range(10):
    importlib.reload(aula98_m)
    print(i)

print('Fim')
