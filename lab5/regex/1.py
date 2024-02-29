import re
pattern = r'ab*'
string = input()
if re.fullmatch(pattern, string):
    print("Match")
else:
    print("No match")
