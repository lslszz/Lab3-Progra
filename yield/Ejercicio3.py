class Cuadrados:
    def __iter__(self):
        for i in range(1, 11):
            yield i ** 2
for c in Cuadrados():
    print(c)