import re
string = input()
temp = re.findall('[A-Z][^A-Z]*', string)
print(temp)
