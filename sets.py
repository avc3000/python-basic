# Sets -> Cannot be deleted
my_set = set()
my_other_set = {}  # Initially is dictionary

print(type(my_set))
print(type(my_other_set))

my_other_set = {"Antony", "Villa", 30}
print(type(my_other_set))
print(len(my_other_set))

my_other_set.add("Colors")
print(my_other_set)  # It isn´t an ordered structure
my_other_set.add("Colors")
print(my_other_set)  # It isn´t supports repeated elements

print("Antony" in my_other_set)
print("John" in my_other_set)

my_other_set.remove("Antony")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

my_set = {"Antony", "Peru", 30}
my_list = list(my_set)
print(type(my_list))

my_other_set = {"C#", "Java", "Java Script"}
my_new_set = my_set.union(my_other_set)
print(my_new_set.union({"Swift"}))
print(my_new_set.difference(my_set))
