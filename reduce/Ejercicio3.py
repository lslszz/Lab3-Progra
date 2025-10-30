from functools import reduce

numeros = [7, 3, 9, 1, 5]
mayor = reduce(lambda x, y: x if x > y else y, numeros)
print(mayor)
