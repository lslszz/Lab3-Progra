from functools import reduce

numeros = [2, 3, 4]
producto = reduce(lambda x, y: x * y, numeros)
print(producto)
