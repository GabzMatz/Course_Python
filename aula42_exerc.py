frase = "O python e uma linguagem de programacao".lower()
ind= 0
fraselen = len(frase)
letra_max= ""
nmr_letra_max = 0

while ind < fraselen:
    caracter = frase[ind]
    
    if caracter == " ":
        ind += 1
        continue

    max_caracter = frase.count(caracter)
    
    if nmr_letra_max > max_caracter:
        letra_max = caracter
    ind += 1
print(f"A letra que mais apareceu foi {letra_max} Aparecendo {nmr_letra_max}")
