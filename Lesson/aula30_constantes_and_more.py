"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = input("digite sua velocidade")  # velocidade atual do carro
local_carro = input("Qual km")  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega



if velocidade > RADAR_1:
    print("Voce passo do limite")
else:
    print("voce nao passsou do limite")

if local_carro >= (LOCAL_1 + RADAR_RANGE) or RADAR_1 < velocidade:
    print("voce sera multado")
else:
    print("nao fez merda")
    

#forma que eu fiz porem a forma certa seria de cima

"""

if int(velocidade) >= RADAR_1 and int(local_carro) >= 99:
    print(f"Voce passou da velodicade")

else:
    print("Ok")

"""