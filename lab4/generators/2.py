def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

n = int(input())
even_gen = even_numbers(n)
even_numbers_s = ', '.join(str(num) for num in even_gen)
print(even_numbers_s)

