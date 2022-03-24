keys = input("Enter your first name: ")
values = input("Enter your last name: ")
my_dict = {}
def upd_dict(keys, values):
    ele = int(input("How many elements do you want? "))
    for i in range(ele):
        keys = input("first_name: ")
        values = input("lastname: ")
        my_dict.update({keys : values})
    print(my_dict)
upd_dict(keys, values)



