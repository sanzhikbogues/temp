def count(n):
    while n >= 0:
        yield n
        n -= 1
n = int(input())
for number in count(n):
    print(number)
