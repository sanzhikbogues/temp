n = input()
numbers_list = list(map(int, n.split()))
x = 1
for i in numbers_list:
    x *= i
print(x)

