string = input()
words = string.split('_')
camel_case_str = words[0] + ''.join(word.title() for word in words[1:])
print(camel_case_str)
