from functools import reduce

palabras = ["Hola", " ", "Mundo", "!"]
frase = reduce(lambda x, y: x + y, palabras)
print(frase)