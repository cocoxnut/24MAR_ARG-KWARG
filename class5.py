user_file = input("Enter name of your file: ")
def file_ext(user_file):
    with open(user_file + '.py', 'w') as file:
        file.write("Hello All")
file_ext(user_file)
read_file = open(user_file + '.py', 'r')
a = read_file.read()
print(a)