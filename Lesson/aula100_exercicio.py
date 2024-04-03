# copy, sorted, produtos.sort
# Exercícios
# 1Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
from hmac import new


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


new_products= [{**product, "preco":round(product["preco"]+(product["preco"] * 0.1))
                }for product in produtos]
print(new_products)



"""new_products = produtos.copy()
for i in new_products:
    i["preco"] =i["preco"]+i["preco"]*0.1
    new_price = i["preco"]
    new_price = f"{new_price:.2f}"
    i["preco"] = new_price
print(new_products)
"""





# 2-Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)


"""new_products = produtos.copy()
for i in new_products:
    i["nome"] = input("Digite algo:\n")
new_products.sort(reverse=True, key=lambda valor : len(valor["nome"]))
print(new_products)
"""



# 3-Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
"""new_products = produtos.copy()
new_products.sort(key=lambda value : value["preco"])
print(new_products)
"""