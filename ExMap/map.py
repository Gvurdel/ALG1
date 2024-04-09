def dobrar_valor(x):
    return x * 2

# Lista de números
numeros = [1, 2, 3, 4, 5]

# Aplicando a função dobrar_valor a cada elemento da lista usando map
dobro = map(dobrar_valor, numeros)

# Convertendo o resultado para uma lista e imprimindo
print(list(dobro))
