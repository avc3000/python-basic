# Lists
my_list = list()
my_other_list = []
print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]
print(my_list)
print(len(my_list))

my_other_list = [30, 1.75, "Antony", "Villager"]
print(type(my_other_list))
print(my_other_list[-1])
print(my_other_list[0])
print(my_list.count(30))
print(len(my_other_list))

age, height, name, surname = my_other_list
print(age, height, name)
print(my_list + my_other_list)

my_other_list.append("Lima")
print(my_other_list)

my_other_list.insert(1, 100)
print(my_other_list)

my_other_list.remove("Lima")
print(my_other_list)
print(my_other_list.pop())
print(my_other_list)

del my_list[2]
print(my_list)

my_new_list = my_list.copy()
my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)
