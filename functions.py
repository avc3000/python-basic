# Functions

def my_function():
    print("This is my function")


my_function()
my_function()


def sum_two_numbers(a, b):
    print("Sum:", a + b)


sum_two_numbers(5, 7)
sum_two_numbers(30, 50)
sum_two_numbers("Antony ", "Jordan")
sum_two_numbers(1.75, 2.75)


def sum_two_values_return(a, b):
    return a + b


my_result = sum_two_values_return("Antony", "Jordan")
print(my_result)


def print_name(name, surname):
    print(f"{name} {surname}")


print_name(surname="Antony", name="Jordan")


def print_name_with_default(name, default, alias="Engineer"):
    print(f"{name} {default} {alias}")


print_name_with_default("Antony", "Jordan")
print_name_with_default("Antony", "Jordan", "English")


def print_texts(*texts):
    for text in texts:
        print(text.upper())


print_texts("Hello", "Python", "Jordan")
print_texts("Antony")
