vocales = ['a', 'e', 'i', 'o', 'u']
frase = input("Escriba una frase: ")
palabra = frase.lower()

contador_vocales = {vocal: palabra.count(vocal) for vocal in vocales}

for vocal, count in contador_vocales.items():
    print(vocal, count)
