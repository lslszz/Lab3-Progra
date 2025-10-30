from functools import reduce

numeros = [5, 10, 15, 20]
suma = reduce(lambda x, y: x + y, numeros)
print(suma) 