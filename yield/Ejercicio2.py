def impares_yield(lista):
    for num in lista:
        if num % 2 != 0:
            yield num
nums = [1,2,3,4,5,6,7,8,9]
for n in impares_yield(nums):
    print(n)