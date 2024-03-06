import string

def generate():
    for i in string.ascii_uppercase:
        file = f"{i}.txt"
        with open(file, 'w'):
            pass
generate()
