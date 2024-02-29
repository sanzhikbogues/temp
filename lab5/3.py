import re
pattern = r'[a-z]+_[a-z]+'
string = input()
matches = re.findall(pattern, string)
print(matches)
