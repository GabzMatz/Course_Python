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




nome=input("Digite seu nome")
nome_num= len(nome)
alterador = 0
meio="*"
meio_alt = 0
meio_like = True
#13


try:
    while alterador < 19:
        print(nome[alterador])
        alterador += 1
        while meio_alt < 1:
            print(meio)
            if meio_like == True:
                meio_like =+ 1
                break
except:
    print("Seu nome separado")
"""
nome="Gabriel Matos"
contador = 0
nome_n=len(nome)
new_name = ""

try:
    while contador < 20:
        letra = nome[contador]+"*"
        new_name += letra
        contador +=  1

        continue
except:
    print("Seu nome separado",new_name)