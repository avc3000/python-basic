# Variables used
my_str_var = 'String variable'
print(my_str_var)

my_int_var = 5
print(my_int_var)

my_int_str_var = str(my_int_var)
print(my_int_str_var)
print(type(my_int_str_var))

my_bool_var = False
print(my_bool_var)

# Concatenate in a print
print(my_str_var, my_int_var, my_int_str_var, my_bool_var)
print('The variable is:', my_bool_var)

# Functions of system
print(len(my_str_var))

# Variables in any line
name, surname, alias, age = "Antony", "Villa", "Tony", 30
print("My name is:", name, surname, "My alias is:", alias, "My age is:", age)

# Input
name = input('What is your name? ')
age = input('What is your age? ')
print(name, age)

# Not strong typing
address: str = "My address"
address = 10.5
print(type(address))
