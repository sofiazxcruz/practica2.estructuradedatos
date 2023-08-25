numeros = [1, 11, 12, 7, 9, 10, 20, 2, 24, 200, 15, 10, 7, 5, 8]

pares = [number for number in numeros if number % 2 == 0]
impares = [number for number in numeros if number % 2 != 0]

print("Serie: ", numeros)
print("Pares: ", pares)
print("Impares: ", impares)
