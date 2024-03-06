def is_palindrome(str):
    str = ''.join(char for char in str)
    return str== str[::-1]
str = input()
if is_palindrome(str):
    print("Palindrome")
else:
    print("Not palindrome")
