def fibonacci():
    a, b = 0, 1
    count = 0
    while count < 10:
        yield a
        a, b = b, a + b
        count += 1
for f in fibonacci():
    print(f)