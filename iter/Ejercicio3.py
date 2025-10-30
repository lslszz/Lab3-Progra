class CuadradosLista:
    def obtener_lista(self):
        return [i**2 for i in range(1, 11)]
print(CuadradosLista().obtener_lista())