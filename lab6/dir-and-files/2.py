import os
def check(path):
    if os.path.exists(path):
        print(f"Path '{path}' exists.")
        if os.access(path, os.R_OK):
            print(f"Path '{path}' is readable.")
        else:
            print(f"Path '{path}' is not readable.")

        if os.access(path, os.W_OK):
            print(f"Path '{path}' is writable.")
        else:
            print(f"Path '{path}' is not writable.")

        if os.access(path, os.X_OK):
            print(f"Path '{path}' is executable.")
        else:
            print(f"Path '{path}' is not executable.")
    else:
        print(f"Path '{path}' does not exist.")
path = input()
check(path)
