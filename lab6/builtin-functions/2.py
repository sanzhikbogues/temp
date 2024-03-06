def count(str):
    upper = 0
    lower = 0
    for char in str:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1

    return (upper, lower)

str = input()
(upper, lower) = count(str)
print(upper)
print(lower)
