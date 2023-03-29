# Conditionals

my_condition = False

if my_condition:
    print("Execute the condition")

my_condition = 5 * 2

if my_condition == 10:
    print("The condition is same of 10")

if my_condition > 11 and my_condition < 20:
    print("Is mayor of 10")
else:
    print("Is minor of 10")

if my_condition < 10:
    print("The condition is minor of 10")
elif my_condition > 10:
    print("The condition is mayor of 10")
else:
    print("The condition is same of 10")

my_new_condition = "Antony"

if len(my_new_condition) != len("Antony") or my_new_condition == "Antony":
    print("The new condition is same")

my_string = ""

if not my_string:
    print("My string is empty")
elif my_string.isnumeric():
    print("The string is number")
else:
    print("The string is not empty")

print("The execution continue")
