import re
str = input()
new_str = re.sub(r'[ ,.]', ':', str)
print(new_str)
