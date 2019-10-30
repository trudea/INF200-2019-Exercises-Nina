def even_numbers(n):
    return [number for number in range(n) if number % 2 == 0]

def even_numbers_gen(n):
    for number in range(n):
        if number % 2 == 0:
            yield number

def odd_numbers(n):
    number = 0
    while True:
        number += 1
        if number >= n:
            return
        elif number % 2 == 1:
            yield number

for i in odd_numbers(10):
    print(i)