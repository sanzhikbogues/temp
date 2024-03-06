def write_list_to_file(path, list):
        with open(path, 'w') as file:
            for i in list:
                file.write(str(i) + '\n')
        print("Done with writing lines to file")
list = [1, 2, 3, 4, 5]
path = input()
write_list_to_file(path, list)
