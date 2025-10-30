class Mayusculas:
    def __init__(self, lista):
        self.lista = lista
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.lista):
            resultado = self.lista[self.index].upper()
            self.index += 1
            return resultado
        raise StopIteration
palabras = ["hola", "mundo", "python"]
for p in Mayusculas(palabras):
    print(p)
