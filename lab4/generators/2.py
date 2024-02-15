def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

n = int(input())
even_gen = even_numbers(n)
temp = ", ".join(str(num) for num in even_gen)
print(temp)