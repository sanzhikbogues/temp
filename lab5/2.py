import re
pattern = r'ab{2,3}'
string = input()
if re.fullmatch(pattern, string):
    print("Match")
else:
    print("No match")
