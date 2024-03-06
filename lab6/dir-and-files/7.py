def copy_file(source_file, destination_file):
    with open(source_file, 'r') as source:
        contents = source.read()
    with open(destination_file, 'w') as destination:
        destination.write(contents)
    print("Copied")
source= input()
destination = input()
copy_file(source, destination)
