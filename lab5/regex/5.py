import re
patt = r'a.*b$'
string = input()
if re.fullmatch(patt, string):
    print("Match")
else:
    print("No match")
