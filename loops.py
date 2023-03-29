### Loops ###

# While
my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else:
    print("My condition is mayor or same 10")

while my_condition < 20:
    my_condition += 1

    if my_condition == 15:
        print("My condition is 15")
        break

    print("My condition is minor of 20")

print("The execution continue WHILE")

# For

my_list = [10, 20, 30, 40, 50]

for element in my_list:
    print("Element list:", element)

my_tuple = (30, 1.75, "Antony", "Villa")

for element in my_tuple:
    print("Element tuple:", element)

my_set = {"Antony", "Villa", 30}

for element in my_set:
    print("Element set:", element)

my_dict = {"Name": "Antony", "Surname": "Villa", "Age": 30}

for element in my_dict.values():
    print("Element dict:", element)

    if element == "Antony":
        break
else:
    print("The loop for dictionary to finished")

for element in my_dict.values():
    print("Element dict:", element)

    if element == "Antony":
        continue
else:
    print("The loop for dictionary to finished")

print("The execution continue FOR")
