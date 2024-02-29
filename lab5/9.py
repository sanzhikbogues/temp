import re
string = input()
new_string = re.sub(r'([a-z])([A-Z])', r'\1 \2', string)
print(new_string)
