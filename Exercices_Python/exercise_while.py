nome="Gabriel Matos Antiqueira"
new_name=""
new_name=""
seletor = 0
"""
    forma com while
while seletor < len(nome):
    digito=nome[seletor]
    new_name += digito
    new_name += "*"
    seletor += 1
print(new_name)



mesma coisa so quem em for
"""
for i in nome:
    new_name += i + "*"

print(new_name)