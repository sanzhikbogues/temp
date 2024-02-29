import re
string = input()
snake_case = re.sub(r'(?<!^)(?=[A-Z])', '_', string).lower()
print("Snake case string:", snake_case)
