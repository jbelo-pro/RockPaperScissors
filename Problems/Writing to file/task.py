f_name = "test.txt"
my_string = "A string to be written to a file!"

# what to do with the file and the string
with open(f_name, 'w') as f:
    print(my_string, file=f)
