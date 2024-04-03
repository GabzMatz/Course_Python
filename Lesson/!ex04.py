"""
Iterando strings com while

#       012345678910
nome = 'Luiz Otávio'  # Iteráveis
#      1110987654321
tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)
print(nome[3])

nova_string = ''
nova_string += '*L*u*i*z* *O*t*á*v*i*o'

"""
# Forma com laco for
"""nome = "Gabriel Matos Antiqueira"
nomeast = ""
for ast in nome:
    nomeast += ast + "*"
print(nomeast)

"""

# Forma com laco while

nome = "Gabriel Matos Antiqueira"
chave = 0
nomeast = ""
while True:
    if len(nome) != chave:
        nomeast += nome[chave]
        nomeast += "*"
        chave += 1
    else:
        print(nomeast)
        break