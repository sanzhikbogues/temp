import os
def delete(path):
    if not os.path.exists(path):
        print(f"'{path}' does not exist.")
        return
    if not os.access(path, os.W_OK):
        print(f"You do not have permission to delete '{path}'")
        return
    os.remove(path)
    print(f"File '{path}' was deleted successfully.")
path = input()
delete(path)