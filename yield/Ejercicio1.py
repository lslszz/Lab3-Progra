def pares():
    for i in range(10):
        yield i * 2
for n in pares():
    print(n)