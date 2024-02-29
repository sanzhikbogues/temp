import re
pattern = r'[A-Z][a-z]+'
string = input()
matches = re.findall(pattern, string)
print(matches)
