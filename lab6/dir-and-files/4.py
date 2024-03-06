def count(path):
        with open(path, 'r') as file:
            lines = sum(1 for line in file)
            print(lines)
path = input()
count(path)
