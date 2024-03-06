import os
def print_files(path):
    print("Directories:")
    for i in os.listdir(path):
        if os.path.isdir(os.path.join(path, i)):
            print(i)

    print("\nFiles:")
    for i in os.listdir(path):
        if os.path.isfile(os.path.join(path, i)):
            print(i)

    print("\nAll Directories and Files:")
    for i in os.listdir(path):
        print(i)

path = input()
print_files(path)
