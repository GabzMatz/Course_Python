palavra_secreta = 'parabolica'
letras_salvas = ''
while True:
    palavra_formando = ''
    letra = input('Digite uma letra:\n')
    if len(letra) == 1 and letra.isalpha():
        if letra in palavra_secreta:  
            letras_salvas += letra
            for ast in palavra_secreta:
                if ast in letras_salvas:
                    palavra_formando += ast
                else:
                    palavra_formando += "*"
            print(palavra_formando)
            if palavra_formando == palavra_secreta:
                print("Parabens a palavra secreta era:\n"+palavra_formando.capitalize().strip())
                break
        else:
            ...
    else:
        print("digite apenas uma letra")