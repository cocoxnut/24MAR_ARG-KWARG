dish = input("What would you like to eat? ")
drinks = input("What would you like to drink? ")
def menu_file(dish, drinks):
	with open('menu.txt', 'w') as menu:
		menu.writelines([f'Customer dish is {dish} and drinks is {drinks}'])
menu_file(dish, drinks)
read_menu = open('menu.txt', 'r')
a = read_menu.read()
print(a)

